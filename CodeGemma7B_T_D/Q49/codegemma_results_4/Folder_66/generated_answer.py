def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    binary_str_len = len(binary_string)
    max_dec = int(binary_string, 2)
    fib_len = 120
    prev_fib_num = 0
    current_fib_num = 1
    current_elem_ind = 1
    while current_fib_num <= max_dec:
        current_elem_ind += 1
        previous_fib_num, current_fib_num = (current_fib_num, fibonacci(current_elem_ind))
    return max_dec % current_fib_num == 0