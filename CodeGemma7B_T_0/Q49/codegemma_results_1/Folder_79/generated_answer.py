def if_decimal_is_divisible(binary_str):

    def get_fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return get_fib(n - 1) + get_fib(n - 2)

    def get_binary_to_decimal(binary_str):
        decimal = 0
        for i in range(len(binary_str)):
            decimal += int(binary_str[i]) * 2 ** (len(binary_str) - i - 1)
        return decimal

    def get_nth_fib_in_binary(n):
        return bin(get_fib(n))[2:]

    def is_divisible(num, divisor):
        return num % divisor == 0
    binary_to_decimal = get_binary_to_decimal(binary_str)
    fib_list = [get_nth_fib_in_binary(i) for i in range(13)]
    for fib in fib_list:
        if is_divisible(binary_to_decimal, get_binary_to_decimal(fib)):
            return True
    return False