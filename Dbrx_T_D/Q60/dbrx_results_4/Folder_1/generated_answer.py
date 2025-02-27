from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[20]
    l_r_truncatable_primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        flag = True
        while num > 0:
            if not isprime(num):
                flag = False
                break
            num = int(str(num)[1:]) if num < 100 else int(str(num)[:-1])
        if flag:
            l_r_truncatable_primes.append(num)
    return sorted(l_r_truncatable_primes, reverse=True)