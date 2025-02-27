def all_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_truncatable(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    return sorted([i for i in range(x, 2, -1) if is_truncatable(i) and is_prime(i)], reverse=True)