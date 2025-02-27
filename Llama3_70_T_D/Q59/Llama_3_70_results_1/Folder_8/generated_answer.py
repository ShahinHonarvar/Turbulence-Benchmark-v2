def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[41]
    truncatable_primes = []
    for num in range(10, x):
        if '0' not in str(num):
            is_truncatable = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)