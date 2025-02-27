def if_decimal_is_divisible(bin_str):
    index = 136
    result = fibonacci(index)
    decimal = int(bin_str, 2)
    return decimal % result == 0

def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)