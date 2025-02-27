def all_left_right_truncatable_prime(n_list):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = n_list[94]
    return sorted([i for i in range(2, x) if is_prime(i) and is_prime(int(str(i)[1:-1]))])