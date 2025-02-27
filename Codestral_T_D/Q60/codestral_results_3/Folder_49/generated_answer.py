def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            if is_left_right_truncatable_prime(num):
                primes.append(num)
    return sorted(primes)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if '0' in str(num):
        return False
    original_num = num
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[1:])
        if num > 0 and num < 10:
            break
    num = original_num
    while num > 0:
        if not is_prime(num):
            return False
        num = int(str(num)[:-1])
        if num > 0 and num < 10:
            break
    return True