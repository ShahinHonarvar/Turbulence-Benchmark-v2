from sympy import isprime

def all_left_right_truncatable_prime(x):
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        str_i = str(i)
        if not '0' in str_i and isprime(i):
            left_truncatable = True
            right_truncatable = True
            for j in range(1, len(str_i)):
                if not isprime(int(str_i[j:])):
                    left_truncatable = False
                    break
            for j in range(0, len(str_i) - 1):
                if not isprime(int(str_i[j:len(str_i)])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)