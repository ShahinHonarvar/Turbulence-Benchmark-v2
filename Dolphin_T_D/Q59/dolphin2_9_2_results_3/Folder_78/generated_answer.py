def all_left_truncatable_prime(t):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = t[23]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            str_i = str(i)
            if '0' not in str_i:
                for j in range(len(str_i)):
                    if not is_prime(int(str_i[j:])):
                        break
                else:
                    primes.append(i)
    return primes