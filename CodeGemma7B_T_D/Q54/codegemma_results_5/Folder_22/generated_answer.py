from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[85]
    result = []
    for i in range(x):
        if isprime(i):
            j = 10
            k = i
            while k > 0:
                if not isprime(k):
                    break
                k = int(str(k)[:-j])
                j *= 10
                if j > 10 ** 5:
                    break
            else:
                result.append(i)
    return sorted(result)