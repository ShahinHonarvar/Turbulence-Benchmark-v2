def all_right_truncatable_prime(tup):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_last_digit(n):
        return n // 10
    x = tup[429]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            temp = i
            while temp > 1:
                if not is_prime(temp):
                    break
                temp = remove_last_digit(temp)
            else:
                primes.append(i)
    return sorted(primes, reverse=True)