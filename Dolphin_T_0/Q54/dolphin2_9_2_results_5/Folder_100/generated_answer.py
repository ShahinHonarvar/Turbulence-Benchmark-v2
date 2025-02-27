def all_right_truncatable_prime(args):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = args[26]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
                if temp == 0:
                    primes.append(i)
                    break
    return sorted(primes)