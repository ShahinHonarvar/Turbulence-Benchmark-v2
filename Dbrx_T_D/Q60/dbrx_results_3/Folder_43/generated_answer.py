from sympy import isprime

def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[89]
    prime_list = [i for i in range(2, x + 1) if isprime(i)]
    lr_truncatable_prime = []
    for prime in prime_list:
        digits = len(str(prime))
        for i in range(1, digits):
            if not isprime(int(str(prime)[i:])):
                break
        else:
            for j in range(1, digits):
                if not isprime(int(str(prime)[:-j])):
                    break
            else:
                if digits > 1 and '0' not in str(prime):
                    lr_truncatable_prime.append(prime)
    return sorted(lr_truncatable_prime, reverse=True)