def all_left_truncatable_prime(num_tuple):

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = num_tuple[1]
    primes = []
    for num in range(x, 0, -1):
        if is_prime(num) and all((is_prime(int(str(num)[i:])) for i in range(len(str(num))) if str(num)[i:] not in ['', '0'])):
            primes.append(num)
    return sorted(primes, reverse=True)