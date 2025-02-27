def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def leading_zeros(n):
        return not '0' in str(n)
    x, = num_tuple
    primes = []
    for num in range(2, x):
        if is_prime(num) and leading_zeros(num):
            trunc = num
            while trunc > 0:
                if not is_prime(trunc):
                    break
                trunc = int(str(trunc)[1:])
            else:
                primes.append(num)
    return sorted(primes)