def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def lefttrunc(n):
    length = len(str(n))
    result = []
    for i in range(1, length):
        p = int(str(n)[:i])
        result.append(p)
    return result

def all_left_truncatable_prime(n):
    result = []
    for i in range(2, n):
        if isprime(i):
            temp = lefttrunc(i)
            check = True
            for j in temp:
                if not isprime(j):
                    check = False
                    break
            if check:
                result.append(i)
    return sorted(result, reverse=True)