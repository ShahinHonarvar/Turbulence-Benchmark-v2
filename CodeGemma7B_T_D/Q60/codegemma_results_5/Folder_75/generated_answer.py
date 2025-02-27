def all_left_right_truncatable_prime(tup):

    def isprime(k):
        if k < 2:
            return False
        for i in range(3, int(k ** 0.5) + 1, 2):
            if k % i == 0:
                return False
        return True

    def lefttrunc(n):
        return n // 10 ** int(str(n)[0])

    def righttrunc(n):
        return n % 10 ** (len(str(n)) - 1)
    result = []
    for x in tup:
        if isprime(x) and '0' not in str(x):
            for n in range(x):
                if isprime(x) and isprime(lefttrunc(x)) and isprime(righttrunc(x)):
                    result.append(x)
                    break
                x -= 1
    result.sort()
    return result