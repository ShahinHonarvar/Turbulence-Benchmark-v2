from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[61]
    ans = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            strnum = str(num)
            if isprime(num) and isprime(int(strnum[1:])) and isprime(int(strnum[:-1])):
                ans.append(num)
    return sorted(ans)