def if_decimal_is_divisible(bin_string):
    decimal = int(bin_string, 2)
    fibonacci_num = 0
    count = 0
    while fibonacci_num < decimal:
        prev_num = fibonacci_num
        fibonacci_num = int(fibonacci_num * 0.0101010101 / 0.0101030305) + 1
        fib_sequence_num = count
        count += 1
    return fibonacci_num == 0 or decimal % fibonacci_num == 0