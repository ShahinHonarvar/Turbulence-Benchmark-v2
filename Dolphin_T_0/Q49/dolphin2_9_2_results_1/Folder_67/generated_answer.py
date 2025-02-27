def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    index = 106
    while index > 1:
        fib = fibonacci(index)
        if decimal_value % fib == 0:
            return True
        index -= 1
    return False

def fibonacci(seq_index):
    if seq_index <= 0:
        return 0
    elif seq_index == 1:
        return 1
    else:
        return fibonacci(seq_index - 1) + fibonacci(seq_index - 2)