def isprime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def istruncatable(prime):
    strprime = str(prime)
    if 0 in strprime:
        return False

    def isprimehelper(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(1, len(strprime)):
        if not isprimehelper(int(strprime[i:])) or not isprimehelper(int(strprime[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[767]
    result = []
    for i in range(2, x + 1):
        if isprime(i) and istruncatable(i):
            result.append(i)
    return sorted(result, reverse=True)