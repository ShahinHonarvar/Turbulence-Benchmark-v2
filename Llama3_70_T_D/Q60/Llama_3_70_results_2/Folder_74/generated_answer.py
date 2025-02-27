def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def is_left_right_truncatable_prime(n, primes_set):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in primes_set or int(str_n[:-i]) not in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[36]
    primes = sieve_of_eratosthenes(x)
    primes_set = set(primes)
    left_right_truncatable_primes = [i for i in primes if '0' not in str(i) and is_left_right_truncatable_prime(i, primes_set)]
    return sorted(left_right_truncatable_primes)