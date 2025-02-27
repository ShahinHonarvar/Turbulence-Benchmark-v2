def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1 or '0' in str(n):
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_lr_truncatable(n):
        if not is_prime(n):
            return False
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:i])) for i in range(1, len(s))))
    x = num_tuple[466]
    return sorted([i for i in range(2, x + 1) if is_lr_truncatable(i)], reverse=True)