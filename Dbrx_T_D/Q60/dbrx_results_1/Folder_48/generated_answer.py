from sympy import isprime

def all_left_right_truncatable_prime(n_tuple):

    def is_left_right_truncatable_prime(num):
        if '0' in str(num) or num < 10:
            return False
        while num > 10:
            if not isprime(num):
                return False
            num = int(str(num)[1:]) if str(num)[0] == '1' else int(str(num)[:-1])
        return isprime(num)
    x = n_tuple[835]
    result = [i for i in range(1, x + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result)