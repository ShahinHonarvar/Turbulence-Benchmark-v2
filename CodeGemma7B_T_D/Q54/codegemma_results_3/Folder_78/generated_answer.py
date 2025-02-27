def all_right_truncatable_prime(args):
    x = args[23]
    result = []

    def isprime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for i in range(2, x):
        if isprime(i):
            num = i
            while num > 0:
                if not isprime(num):
                    break
                num //= 10
            else:
                result.append(i)
    return sorted(result)