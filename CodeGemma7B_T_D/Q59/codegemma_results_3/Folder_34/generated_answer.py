from sympy import primerange

def all_left_truncatable_prime(args0):
    ans = []
    for i in args0[18]:
        if is_prime(i) and (not contains_zero(i)):
            truncatable = True
            for j in str(i)[1:]:
                if not is_prime(int(j)):
                    truncatable = False
                    break
            if truncatable:
                ans.append(i)
    ans.sort(reverse=True)
    return ans

def is_prime(i):
    return sympy.isprime(i)

def contains_zero(i):
    return '0' in str(i)