def if_decimal_is_divisible(binary):
    fib_num = generate_fibonacci_up_to_index(binary)
    num = int(binary, 2)
    return num % fib_num == 0

def generate_fibonacci_up_to_index(binary):
    fib_num = 0
    counter = 2
    len_bin_num = len(binary)
    while fib_num <= len_bin_num:
        if fib_num == len_bin_num:
            return fib_num
        fib_num += counter
        counter += 1