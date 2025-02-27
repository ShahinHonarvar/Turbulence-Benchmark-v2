def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_right_truncate(num):
    left_truncatable = True
    temp = num
    while temp > 9:
        temp //= 10
        if not is_prime(temp):
            left_truncatable = False
            break
    right_truncatable = True
    temp = num
    while temp > 9:
        temp //= 10
        temp = int(str(temp)[0])
        if not is_prime(temp):
            right_truncatable = False
            break
    return left_truncatable and right_truncatable

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    for num in numbers:
        if num > 1 and left_right_truncate(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)