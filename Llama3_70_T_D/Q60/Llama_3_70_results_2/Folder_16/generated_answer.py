def all_left_right_truncatable_prime(numbers):
    x = numbers[792]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        n_str = str(n)
        for _ in range(len(n_str) - 1):
            n_str = n_str[1:-1]
            if not is_prime(int(n_str)) or '0' in n_str:
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result)