def if_decimal_is_divisible(binary_string):
    if len(binary_string) == 0 or len(binary_string) == 1:
        return False
    binary_int = int(binary_string, 2)
    fibonacci_dict = {0: 0, 1: 1}
    fibonacci_num = 2
    fib_index = 2
    while fibonacci_num <= binary_int:
        fibonacci_dict[fib_index] = fibonacci_dict[fib_index - 1] + fibonacci_dict[fib_index - 2]
        fibonacci_num = fibonacci_dict[fib_index]
        fib_index += 1
    if binary_int % fibonacci_dict[48] == 0:
        return True
    else:
        return False