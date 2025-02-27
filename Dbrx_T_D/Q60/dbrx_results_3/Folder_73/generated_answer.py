from sympy import isprime

def all_left_right_truncatable_prime(number_tuple):
    x = number_tuple[97]
    l_r_truncatable_primes = []
    for num in range(2, x + 1):
        if not isprime(num) or '0' in str(num):
            continue
        flag = True
        while num > 9:
            num = int(str(num)[1:]) if str(num)[0] == '1' else int(str(num)[1:] or 1)
            if not isprime(num):
                flag = False
                break
        if flag:
            l_r_truncatable_primes.append(str(num))
    return sorted(list(map(int, l_r_truncatable_primes)))