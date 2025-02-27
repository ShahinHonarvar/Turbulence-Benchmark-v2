from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):
    x = n_tuple[55]
    l_and_r_truncatable_primes = []
    for num in range(1, x + 1):
        if not str(num).startswith('0') and isprime(num):
            left_num = int(str(num)[1:])
            while left_num > 0:
                if not isprime(left_num):
                    break
                left_num = int(str(left_num)[1:])
            else:
                right_num = num
                while len(str(right_num)) > 1:
                    if not isprime(right_num):
                        break
                    right_num = int(str(right_num)[:-1])
                else:
                    l_and_r_truncatable_primes.append(num)
    return sorted(l_and_r_truncatable_primes, reverse=True)