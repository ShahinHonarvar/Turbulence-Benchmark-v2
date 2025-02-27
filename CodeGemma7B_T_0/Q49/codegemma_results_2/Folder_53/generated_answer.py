def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num + 1
        return get_next_fib(get_next_fib(num - 1)) + get_next_fib(num - 2)

    def get_binary_of_num(num):
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            if num % 2 == 0:
                result = '0' + result
            else:
                result = '1' + result
            num //= 2
        return result

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_of_fib = get_binary_of_num(get_next_fib(64))
    return is_divisible(int(binary_str, 2), int(binary_of_fib, 2))