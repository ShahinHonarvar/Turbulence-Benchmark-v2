from sympy import isprime

def all_left_right_truncatable_prime(x):
    ans = []
    for n in range(2, x + 1):
        if n < 100 or (n >= 1000 and n % 5 == 0):
            continue
        if len(str(n)) > 1 and '0' in str(n):
            continue
        nStr = str(n)
        if isprime(n) and isprime(nStr[0]):
            for i in range(1, len(nStr)):
                if not isprime(int(nStr[i:])):
                    break
                else:
                    for j in range(1, len(nStr) - i + 1):
                        if not isprime(int(nStr[j:i + j])):
                            break
                    else:
                        ans.append(n)
    return sorted(ans, reverse=True)