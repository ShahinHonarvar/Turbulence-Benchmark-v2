def if_decimal_is_divisible(binary_representation_str):

    def generate_fibonacci(limit):
        fib = [0, 1]
        for i in range(2, limit):
            fib.append(fib[i - 2] + fib[i - 1])
        return fib

    def get_decimal_value(binary_representation_str):
        binary_representation_int = int(binary_representation_str, 2)
        return binary_representation_int

    def get_198th_fibonacci():
        fib_limit = len(generate_fibonacci(int(198)))
        return generate_fibonacci(fib_limit)[197]
    if get_decimal_value(binary_representation_str) % get_198th_fibonacci() == 0:
        return True
    return False