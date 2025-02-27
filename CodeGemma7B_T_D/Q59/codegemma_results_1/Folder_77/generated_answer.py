from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[767]
    plist = [i for i in range(2, x) if isprime(i) and (not str(i).startswith('0'))]
    result = []
    for p in plist:
        s = str(p)
        q = int(s[1:])
        if (isprime(q) and isprime(int(s[2:])) and isprime(int(s[3:])) and isprime(int(s[4:])) and isprime(int(s[5:])) and isprime(int(s[6:])) and isprime(q)) and q > p:
            result.append(p)
    return sorted(result, reverse=True)