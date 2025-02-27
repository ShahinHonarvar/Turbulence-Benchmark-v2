import sympy

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[42]
    prime_list = []
    for i in range(2, x):
        if sympy.isprime(i):
            num = i
            while num > 0:
                if not sympy.isprime(num):
                    break
                num = int(str(num)[1:])
            else:
                if num != 0:
                    prime_list.append(i)
    return prime_list