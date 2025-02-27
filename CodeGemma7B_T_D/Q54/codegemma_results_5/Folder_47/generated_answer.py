import sympy

def all_right_truncatable_prime(x):
    """
    This function takes an argument that is a tuple of positive integers and returns the sorted list of all right-truncatable prime numbers less than x.
    The function should return an empty list if there is no such right-truncatable prime number.
    """
    '\n    This is an more efficient code which does not use sympy library\n    '
    all_right_truncatable_prime_list = []
    for i in range(2, x):
        s = str(i)
        flag = True
        for j in range(1, len(s)):
            t = int(s[:-j])
            if not sympy.ntheory.isprime(t):
                flag = False
                break
        if flag:
            all_right_truncatable_prime_list.append(i)
    return sorted(all_right_truncatable_prime_list)