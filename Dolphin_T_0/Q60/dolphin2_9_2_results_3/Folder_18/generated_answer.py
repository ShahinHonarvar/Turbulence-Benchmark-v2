from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[429]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        while len(str_num) > 1:
            if not isprime(int(str_num[1:-1])):
                break
            str_num = str_num[1:-1]
            if len(str_num) == 1:
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)