from sympy import isprime

def all_left_truncatable_prime(n_tuple):
    x, = n_tuple
    left_truncatable_prime_list = []
    for i in range(2, x):
        if isprime(i) and str(i).count('0') == 0:
            truncate_i = i
            while truncate_i > 1:
                truncate_i = truncate_i // 10
                if isprime(truncate_i) == False:
                    break
            else:
                left_truncatable_prime_list.append(i)
    left_truncatable_prime_list.sort(reverse=True)
    return left_truncatable_prime_list