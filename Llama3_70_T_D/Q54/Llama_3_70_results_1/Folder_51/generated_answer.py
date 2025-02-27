def all_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    x = args[54]
    primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes)