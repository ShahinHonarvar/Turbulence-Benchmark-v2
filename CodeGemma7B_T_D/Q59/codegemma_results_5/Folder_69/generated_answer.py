from sympy import isprime

def all_left_truncatable_prime(n):
    """
    Returns the list of all left-truncatable prime numbers less than n. The return list should be sorted in descending order.
    """
    res = []
    for num in range(2, n):
        str_num = str(num)
        if '0' not in str_num and isprime(num):
            for i in range(1, len(str_num)):
                if not isprime(int(str_num[i:])):
                    break
            else:
                res.append(num)
    return sorted(res, reverse=True)