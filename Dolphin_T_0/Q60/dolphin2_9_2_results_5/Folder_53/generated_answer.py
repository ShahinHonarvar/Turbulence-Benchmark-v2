def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(num):
        num_str = str(num)
        return is_prime(int(num_str[1:-1])) and (len(num_str) == 2 or check_truncatable(int(num_str[1:-1])))
    x = numbers[86]
    result = [i for i in range(x, 1, -1) if is_prime(i) and check_truncatable(i)]
    return sorted(result, reverse=True)