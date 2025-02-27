def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[20]
    truncatable_primes = []
    for num in range(10, x):
        if '0' not in str(num) and is_prime(num):
            trunc = str(num)
            while len(trunc) > 1:
                trunc = trunc[1:]
                if not is_prime(int(trunc)):
                    break
            else:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)