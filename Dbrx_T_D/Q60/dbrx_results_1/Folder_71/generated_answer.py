from sympy import isprime

def all_left_right_truncatable_prime(x_tuple):
    x = x_tuple[22]
    l_r_truncatable_primes = []
    for num in range(10, x + 1):
        if isprime(num) and '0' not in str(num):
            is_l_r_truncatable_prime = True
            for i in range(1, len(str(num))):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_l_r_truncatable_prime = False
                    break
            if is_l_r_truncatable_prime:
                l_r_truncatable_primes.append(num)
    return sorted(l_r_truncatable_primes, reverse=True)