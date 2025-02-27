def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f += 6
        return True
    x = num_tuple[70]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            if all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
                primes.append(num)
    return sorted(primes)