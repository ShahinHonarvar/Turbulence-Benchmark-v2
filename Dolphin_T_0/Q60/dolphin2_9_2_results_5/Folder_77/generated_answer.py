def all_left_right_truncatable_prime(y):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    x = y[767]
    primes = []
    for i in range(x, 0, -1):
        if '0' in str(i):
            continue
        if is_prime(i):
            if all((is_prime(int(str(i).replace(str(j), ''))) for j in range(1, len(str(i)) - 1))):
                primes.append(i)
    return primes[::-1]