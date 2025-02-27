from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):

    def is_left_right_truncatable_prime(n):
        if '0' in str(n) or not isprime(n):
            return False
        while n > 10:
            n = int(str(n)[1:]) if str(n)[0] == '1' else int(str(n)[:-1])
            if not isprime(n):
                return False
        return True
    limit = nums_tuple[100]
    result = [i for i in range(2, limit + 1) if is_left_right_truncatable_prime(i)]
    return sorted(result)