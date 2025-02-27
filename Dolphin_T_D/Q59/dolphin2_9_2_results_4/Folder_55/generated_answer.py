def all_left_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[73]
    prime_nums = []
    for num in range(x - 1, 0, -1):
        num_str = str(num)
        if '0' not in num_str and all((is_prime(int(num_str[i:])) for i in range(len(num_str)))):
            prime_nums.append(num)
    return sorted(prime_nums, reverse=True)