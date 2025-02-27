def if_decimal_is_divisible(binary_string):
    fib_num = 0
    multiplier = 1
    for digit in binary_string[::-1]:
        fib_num += multiplier * int(digit)
        multiplier *= 2
    if fib_num % 125 == 0:
        return True
    return False