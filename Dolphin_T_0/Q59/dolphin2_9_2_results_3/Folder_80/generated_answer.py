def all_left_truncatable_prime(a_tuple):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        elif n == 2:
            return True
        else:
            for x in range(2, n):
                if n % x == 0:
                    return False
            return True
    x = a_tuple[14]
    left_truncatable_prime_numbers = [i for i in reversed(range(x)) if is_prime(i) and str(i).count('0') == 0 and all((is_prime(int(str(i)[1:])) for j in range(1, len(str(i)))))]
    return left_truncatable_prime_numbers