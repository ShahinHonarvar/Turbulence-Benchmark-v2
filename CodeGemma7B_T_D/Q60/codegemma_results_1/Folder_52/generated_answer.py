from sympy import isprime

def all_left_right_truncatable_prime(n):
    ans = []
    for i in range(2, n + 1):
        if '0' not in str(i) and isprime(i):
            l = r = i
            while l in range(2, int(str(i)[:len(str(i)) // 2]) + 1) and r in range(2, int(str(i)[len(str(i)) // 2:]) + 1):
                l = int(str(i)[:len(str(i)) // 2])
                r = int(str(i)[len(str(i)) // 2:])
                if not (isprime(l) and isprime(r)):
                    break
                if l == 2 or r == 2:
                    ans.append(i)
                    break
                l = int(str(l)[:len(str(l)) // 2])
                r = int(str(r)[:len(str(r)) // 2])
    ans.sort(reverse=True)
    return ans