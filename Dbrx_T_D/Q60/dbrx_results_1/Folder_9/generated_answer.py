from sympy import isprime

def all_left_right_truncatable_prime(tuple_of_pos_int):

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not isprime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    x = tuple_of_pos_int[29]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(result, reverse=True)