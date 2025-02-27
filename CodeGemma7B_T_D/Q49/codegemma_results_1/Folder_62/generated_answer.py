def if_decimal_is_divisible(binary_str):

    def is_divisible_by(num, divisor):
        while num >= divisor:
            num -= divisor
        return num == 0
    fib_div_thirteen = 22050444415045060967179506
    fib_index = 35
    for num in fib_values(binary_str):
        if is_divisible_by(num, fib_div_thirteen):
            return True
        elif num >= fib_div_thirteen:
            fib_index += 1
            fib_div_thirteen = fib_values(binary_str)[fib_index]
    return False

def fib_values(binary_str):
    values = [0, 1]
    length = len(binary_str)
    for index in range(2, length):
        next_value = values[index - 1] + values[index - 2]
        values.append(next_value)
    return values