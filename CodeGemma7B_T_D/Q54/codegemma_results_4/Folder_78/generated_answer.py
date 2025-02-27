from sympy import isprime

def all_right_truncatable_prime(x):
    p = [i for i in range(2, x) if isprime(i)]
    ans = []
    for i in p:
        tmp = i
        while tmp >= 10:
            tmp //= 10
            if not isprime(tmp):
                break
        if tmp in p:
            ans.append(i)
    return sorted(ans)