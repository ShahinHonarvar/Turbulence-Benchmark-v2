from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[33]
    lr_prime = []

    def is_left_right_truncatable(n):
        if str(n)[0] == '0' or not isprime(n):
            return False
        while n > 1:
            n /= 10
            if not isprime(int(n)):
                return False
        return True
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            lr_prime.append(num)
    return sorted(lr_prime)