def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_nth_fibonacci(n):
        if n == 176:
            return fibonacci(n - 1)
        else:
            return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)
    decimal = int(binary, 2)
    return decimal % get_nth_fibonacci(176) == 0