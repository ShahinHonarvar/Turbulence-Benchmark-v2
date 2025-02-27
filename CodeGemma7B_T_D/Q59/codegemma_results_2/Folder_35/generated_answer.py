def all_left_truncatable_prime(t):
    x = t[177]
    result = []
    for i in range(2, x):
        if all((p not in str(i) for p in '0123456789')) and isprime(i):
            if isprime(int(str(i)[1:])):
                if isprime(int(str(i)[2:])):
                    if isprime(int(str(i)[3:])):
                        if isprime(int(str(i)[4:])):
                            if isprime(int(str(i)[5:])):
                                result.append(i)
    return sorted(result)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True