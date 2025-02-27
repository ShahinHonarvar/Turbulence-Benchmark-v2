def if_decimal_is_divisible(binary_representation):
    bin_num = int(binary_representation, 2)
    fib_num = fibonacci(bin_num)
    return fib_num % 107 == 0