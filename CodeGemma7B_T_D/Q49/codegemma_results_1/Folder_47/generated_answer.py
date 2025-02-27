def if_decimal_is_divisible(binary_string):

    def get_fib(n):
        if n in (0, 1):
            return 1
        prev, current = (1, 1)
        for _ in range(2, n):
            prev, current = (current, prev + current)
        return current

    def binary_to_int(binary_string):
        return int(binary_string, 2)

    def is_divisible(decimal_int, divisor):
        return decimal_int % divisor == 0
    fibo_94th_num = get_fib(94)
    binary_int = binary_to_int(binary_string)
    return is_divisible(binary_int, fibo_94th_num)