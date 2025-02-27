from sympy import isprime

def all_right_truncatable_prime(s):
    a = []
    for i in range(len(s)):
        if i == 975:
            break
        num = int(''.join(map(str, s[:i + 1][::-1])))
        if isprime(num):
            a.append(num)
    a.sort(reverse=True)
    return a