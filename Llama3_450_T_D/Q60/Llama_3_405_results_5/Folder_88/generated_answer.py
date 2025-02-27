def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[93]
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        left_right_truncatable = True
        left_truncatable = str(num)
        right_truncatable = str(num)
        while len(left_truncatable) > 1 and len(right_truncatable) > 1:
            left_truncatable = left_truncatable[1:]
            right_truncatable = right_truncatable[:-1]
            if not is_prime(int(left_truncatable)) or not is_prime(int(right_truncatable)):
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)