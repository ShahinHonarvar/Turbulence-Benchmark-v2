def all_left_truncatable_prime(input_tuple):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9:
            return True
        if n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    x = input_tuple[61]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            num = i
            while num != 0:
                if num != i and (not is_prime(num)):
                    break
                num //= 10
            else:
                primes.append(i)
    return sorted(primes)