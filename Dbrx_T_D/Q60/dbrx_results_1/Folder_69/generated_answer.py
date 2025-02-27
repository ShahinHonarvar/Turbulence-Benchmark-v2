from sympy import isprime

def all_left_right_truncatable_prime(tup):
    primes = []
    for num in range(2, tup[760] + 1):
        if not isprime(num):
            continue
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_right_truncatable = True
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)