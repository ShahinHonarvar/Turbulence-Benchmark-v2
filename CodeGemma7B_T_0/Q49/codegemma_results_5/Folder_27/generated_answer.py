def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary):
        decimal = 0
        for i in range(len(binary)):
            decimal += int(binary[i]) * 2 ** i
        return decimal

    def get_nth_fibonacci(n):
        fib_list = [fibonacci(i) for i in range(n + 1)]
        return fib_list[n]
    binary_to_decimal(binary)
    if get_nth_fibonacci(87) % binary_to_decimal(binary) == 0:
        return True
    else:
        return False