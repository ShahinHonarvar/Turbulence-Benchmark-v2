def all_right_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[466]
    primes = []
    for i in range(x):
        if is_prime(i):
            copy_i = i
            while copy_i != 0:
                if not is_prime(copy_i):
                    break
                copy_i = copy_i // 10
            else:
                primes.append(i)
    return sorted(primes, reverse=True)