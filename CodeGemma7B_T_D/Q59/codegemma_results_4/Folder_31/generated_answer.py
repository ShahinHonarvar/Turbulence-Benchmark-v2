from sympy import prime

def all_left_truncatable_prime(b):
    x = b[50]
    ans = []
    ans = [i for i in range(2, x) if prime(i) and str(i)[-1] != '0' and all((prime(int(str(i)[j:i])) for j in range(1, len(str(i)))))]
    return sorted(ans, reverse=True)