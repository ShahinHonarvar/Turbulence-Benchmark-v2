def all_left_right_truncatable_prime(integer_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = integer_tuple[466]
    return sorted([n for n in range(2, x + 1) if is_prime(n) and str(n).count('0') == 0 and all((is_prime(int(str(n)[i:n.index(str(n)[-1])])) for i in range(1, len(str(n)))))], reverse=True)