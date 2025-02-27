def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_and_right_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 2:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:-1]
        return is_prime(int(n_str))
    x = num_tuple[67]
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable_prime(i)], reverse=True)