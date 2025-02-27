from sympy import isprime, nextprime

def all_left_truncatable_prime(t):
    x = t[767]
    res = []
    for i in range(2, x):
        if '0' not in str(i) and isprime(i):
            j = i
            nums = set()
            while j > 9:
                j = nextprime(j)
                nums.add(j)
            nums.add(j)
            k = 10 ** (len(str(j)) - 1)
            if all((isprime(j // k) for j in nums)):
                res.append(i)
    return sorted(res, reverse=True)