from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[71]
    result = []
    for i in range(1, x):
        j = i
        while j > 0:
            if not isprime(j):
                break
            j = j // 10
        if j == 0:
            result.append(i)
    return sorted(result, reverse=True)