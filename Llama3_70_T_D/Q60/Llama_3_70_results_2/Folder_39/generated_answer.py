def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = {i for i in range(2, x + 1) if is_prime(i)}
    truncatable_primes = []
    for p in primes:
        p_str = str(p)
        if '0' not in p_str:
            is_truncatable = True
            for i in range(1, len(p_str)):
                if int(p_str[i:]) not in primes or int(p_str[:-i]) not in primes:
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)