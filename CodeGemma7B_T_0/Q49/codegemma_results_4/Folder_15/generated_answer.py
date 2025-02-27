def if_decimal_is_divisible(binary_str):

    def get_next_fibonacci(num):
        if num in (0, 1):
            return num
        return get_next_fibonacci(num - 1) + get_next_fibonacci(num - 2)

    def get_decimal_value(binary_str):
        decimal_value = 0
        for i, bit in enumerate(binary_str):
            decimal_value += int(bit) * 2 ** i
        return decimal_value

    def get_nth_fibonacci(n):
        fibonacci_nums = [0, 1]
        for i in range(2, n + 1):
            fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
        return fibonacci_nums[n]
    binary_str = binary_str[::-1]
    decimal_value = get_decimal_value(binary_str)
    nth_fibonacci = get_nth_fibonacci(get_next_fibonacci(9))
    return decimal_value % nth_fibonacci == 0