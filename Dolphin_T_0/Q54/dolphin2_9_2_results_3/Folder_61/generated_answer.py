def all_right_truncatable_prime(input_tuple):

    def is_prime(n):
        if n in (2, 3) or (n % 2 != 0 and n % 3 != 0):
            for i in range(5, int(n ** 0.5) + 1, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
        return False
    x = input_tuple[3]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            j = i
            while j != 0 and is_prime(j):
                j = int(j / 10)
            if j == 0:
                right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes