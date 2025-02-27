from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[33]
    l_r_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        string_num = str(num)
        if '0' in string_num:
            continue
        is_l_r_truncatable_prime = True
        for i in range(1, len(string_num)):
            if not isprime(int(string_num[i:])):
                is_l_r_truncatable_prime = False
                break
            if not isprime(int(string_num[:i])):
                is_l_r_truncatable_prime = False
                break
        if is_l_r_truncatable_prime:
            l_r_truncatable_primes.append(num)
    l_r_truncatable_primes.sort()
    return l_r_truncatable_primes