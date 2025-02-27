def if_decimal_is_divisible(binary_str):

    def get_fibonacci(n):
        if n in (0, 1):
            return n
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)

    def get_binary_to_decimal(binary_str):
        return int(binary_str, 2)

    def get_index_of_first_divisible_by_168(fib_list):
        for i, num in enumerate(fib_list):
            if num % 168 == 0:
                return i
        return -1
    fib_list = [get_fibonacci(i) for i in range(get_index_of_first_divisible_by_168(fib_list))]
    decimal_int = get_binary_to_decimal(binary_str)
    return decimal_int % fib_list[get_index_of_first_divisible_by_168(fib_list)] == 0