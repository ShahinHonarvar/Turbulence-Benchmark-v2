def all_right_truncatable_prime(int_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    x = int_tuple[645]
    right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            j = i
            while j != 0:
                if j != i and (not is_prime(j)):
                    break
                j //= 10
            else:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)