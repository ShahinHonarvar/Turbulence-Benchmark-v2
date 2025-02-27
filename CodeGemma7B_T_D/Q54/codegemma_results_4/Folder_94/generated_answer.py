from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[43]
    ans = []
    for num in range(x):
        if isprime(num):
            temp = num
            length = len(str(temp))
            if length <= 1:
                continue
            while length > 1:
                temp = temp // 10
                if temp != 0 and (not isprime(temp)):
                    break
                if isprime(temp):
                    ans.append(num)
                length -= 1
    return sorted(ans)