from sympy import isprime

def all_left_right_truncatable_prime(arg):

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return isprime(n)
        return isprime(n) and is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))
    return sorted([num for num in range(1, arg[29] + 1) if is_left_right_truncatable_prime(num)], reverse=True)