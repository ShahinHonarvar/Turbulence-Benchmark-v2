from sympy import isprime

def all_left_right_truncatable_prime(num):
    ans = []
    for i in range(2, num + 1):
        if isprime(i):
            n = str(i)
            if '0' not in n:
                if all((isprime(int(n[a:b + 1])) for a in range(len(n)) for b in range(a + 1, len(n) + 1))):
                    ans.append(i)
    return sorted(ans, reverse=True)