from sympy import isprime

def all_left_truncatable_prime(x):
    prime = [i for i in range(2, x) if isprime(i) and '0' not in str(i)]

    def del_leading_digit(num):
        if num == 0:
            return -1
        return int(str(num)[1:])
    left_truncatable_primes = sorted([i for i in prime if del_leading_digit(i) in prime], key=int)
    return left_truncatable_primes