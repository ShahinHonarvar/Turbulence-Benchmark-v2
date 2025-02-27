def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num
        return get_next_fib(num - 1) + get_next_fib(num - 2)

    def get_fib_num(index):
        fib_num = 0
        fib_index = 0
        while fib_index <= index:
            if fib_index == index:
                return fib_num
            fib_num = get_next_fib(fib_num)
            fib_index += 1

    def get_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = (decimal << 1) + int(digit)
        return decimal
    return get_decimal(binary_str) % get_fib_num(139) == 0