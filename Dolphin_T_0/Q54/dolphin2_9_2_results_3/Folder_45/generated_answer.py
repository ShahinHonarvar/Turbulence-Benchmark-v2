def all_right_truncatable_prime(a_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = a_tuple[61]
    right_truncatable_primes = [2]
    for i in range(3, x):
        if is_prime(i):
            for j in range(i, 0, -1):
                if j != i and is_prime(int(str(i)[-j:])):
                    right_truncatable_primes.append(i)
                    break
    if len(right_truncatable_primes) == 1 and right_truncatable_primes[0] > x:
        return []
    return sorted(right_truncatable_primes)