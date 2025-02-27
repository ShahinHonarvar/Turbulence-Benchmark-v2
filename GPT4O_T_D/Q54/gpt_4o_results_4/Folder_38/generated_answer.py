import sympy

def all_right_truncatable_prime(data):

    def is_right_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not sympy.isprime(int(str_num)):
                return False
            str_num = str_num[:-1]
        return True
    if len(data) < 29:
        return []
    x = data[28]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)