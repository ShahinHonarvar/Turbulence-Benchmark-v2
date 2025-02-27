def all_left_trunc_primes(n_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = n_tuple[91]
    trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            trunc = str(num)
            while len(trunc) > 1:
                if not all((digit != '0' for digit in trunc[1:])):
                    break
                if not is_prime(int(trunc[1:])):
                    break
                trunc = trunc[1:]
            else:
                trunc_primes.append(num)
    return sorted(trunc_primes)