from sympy import isprime

def all_left_right_truncatable_prime(n):
    """
    n = a tuple of positive integers
    """
    lst = []
    for i in range(1, n[0] + 1):
        if isprime(i) and str(i)[0] == str(i)[-1] and ('0' not in str(i)):
            k = len(str(i))
            while k > 1:
                if not isprime(int(str(i)[:k])):
                    break
                k -= 1
            if k == 0 or k == 1:
                lst.append(i)
    lst.sort(reverse=True)
    return lst