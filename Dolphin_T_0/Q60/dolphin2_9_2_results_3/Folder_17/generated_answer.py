def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        num_str = str(n)
        while len(num_str) > 1:
            if len(num_str) == 2:
                if not is_prime(int(num_str[1])):
                    return False
            else:
                if not is_prime(int(num_str[1:])):
                    return False
                if not is_prime(int(num_str[:-1])):
                    return False
            num_str = num_str[1:-1]
        return is_prime(int(num_str))
    return sorted([n for n in range(x, 0, -1) if is_truncatable_prime(n)], reverse=True)