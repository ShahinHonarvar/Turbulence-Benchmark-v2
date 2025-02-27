def if_decimal_is_divisible(binary_representation):

    def fibonacci_num(num):
        if num == 1:
            return [0, 1]
        temp = fibonacci_num(num - 1)
        temp.append(temp[num - 2] + temp[num - 1])
        return temp
    less_than_59th_fibonacci = fibonacci_num(58)
    base_two = 2
    decimal = 0
    for digit in binary_representation:
        decimal += int(digit) * base_two
        base_two *= 2
    return decimal in less_than_59th_fibonacci