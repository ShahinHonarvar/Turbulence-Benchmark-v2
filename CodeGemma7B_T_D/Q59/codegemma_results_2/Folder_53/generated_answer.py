def all_left_truncatable_prime(tup):

    def isprime(a):
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    def lefttruncatable(a):
        if '0' in str(a):
            return False
        b = str(a)
        for i in range(1, len(b)):
            if isprime(int(b[i:])) == False:
                return False
        return True
    x = tup[86]
    d = []
    for i in range(2, x):
        if isprime(i) and lefttruncatable(i):
            d.append(i)
    d.sort(reverse=True)
    return d