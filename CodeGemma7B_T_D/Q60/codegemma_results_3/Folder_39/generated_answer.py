from sympy import isprime

def all_left_right_truncatable_prime(n):
    out = []
    for i in range(2, n + 1):
        if isprime(i) and '0' not in str(i):
            rem_i = [int(j) for j in str(i)]
            li = len(rem_i)
            for j in range(li):
                if isprime(rem_i[j]):
                    rem_i[j] = rem_i[j] * 10 ** (li - j - 1)
                    if isprime(rem_i[j]):
                        out.append(i)
                else:
                    break
    return sorted(out, reverse=True)