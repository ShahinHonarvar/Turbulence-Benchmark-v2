from sympy import isprime

def all_left_right_truncatable_prime(t):
    primes = []
    x = t[73]
    for num in range(1, x + 1):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_lrtp = True
                for i in range(1, len(str_num)):
                    if not isprime(int(str_num[i:])) or not isprime(int(str_num[:-i])):
                        is_lrtp = False
                        break
                if is_lrtp:
                    primes.append(num)
    return sorted(primes, reverse=True)