def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                return False
        return True
    x = numbers[14]
    result = []
    for num in range(x, 10, -1):
        if is_left_right_truncatable(num):
            result.append(num)
    return result