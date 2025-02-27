def all_left_right_truncatable_prime(tuple_x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = tuple_x[4]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((int(str(num)[i:j + 1]) != 0 and is_prime(int(str(num)[i:j + 1])) for i in range(len(str(num))) for j in range(i, len(str(num))))):
            primes.append(num)
    return primes