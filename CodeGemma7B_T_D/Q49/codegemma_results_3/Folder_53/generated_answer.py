def if_decimal_is_divisible(binary):

    def generate_fibonacci():
        fib = [0, 1]
        temp = 0
        i = 2
        while True:
            temp = fib[i - 1] + fib[i - 2]
            fib.append(temp)
            i += 1
            yield temp

    def convert_binary_to_decimal(binary):
        decimal = int(binary, 2)
        return decimal
    generator = generate_fibonacci()
    Fibonacci_number = next(generator)
    while True:
        Fibonacci_number = next(generator)
        if Fibonacci_number % 64 != 0:
            continue
        else:
            if binary:
                decimal = convert_binary_to_decimal(binary)
                if decimal % Fibonacci_number == 0:
                    return True
            return False