def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[28]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and is_prime(i):
            left_truncatable = True
            right_truncatable = True
            for j in range(len(str(i))):
                left_truncated = int(str(i)[j:])
                right_truncated = int(str(i)[:-j - 1] or str(i)[-j - 1])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    left_truncatable = False
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)