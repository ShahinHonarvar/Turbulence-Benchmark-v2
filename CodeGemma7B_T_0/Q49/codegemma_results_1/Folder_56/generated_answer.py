def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def get_next_fibonacci(current):
        if current == fibonacci(0):
            return fibonacci(1)
        else:
            for i in range(current + 1, fibonacci(len(str(current)) + 1)):
                if fibonacci(i) > current:
                    return fibonacci(i)

    def get_decimal_value(binary):
        decimal = 0
        for i, bit in enumerate(binary):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(decimal, divisor):
        return decimal % divisor == 0
    current_fibonacci = fibonacci(0)
    next_fibonacci = get_next_fibonacci(current_fibonacci)
    decimal = get_decimal_value(binary)
    while True:
        if is_divisible(decimal, current_fibonacci):
            return True
        elif is_divisible(decimal, next_fibonacci):
            return True
        else:
            current_fibonacci = next_fibonacci
            next_fibonacci = get_next_fibonacci(current_fibonacci)