def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    primes = [i for i in range(2, x + 1) if is_prime(i) and '0' not in str(i)]
    truncatable_primes = []
    for p in primes:
        str_p = str(p)
        truncatable = True
        for i in range(1, len(str_p)):
            if not is_prime(int(str_p[i:])) or not is_prime(int(str_p[:-i])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)