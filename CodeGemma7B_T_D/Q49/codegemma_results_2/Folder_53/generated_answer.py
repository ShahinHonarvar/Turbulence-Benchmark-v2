def if_decimal_is_divisible(binary):
    fibonacci_list = [0]
    is_divisible = False
    decimal = 0
    for i in range(1, 65):
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        if decimal + int(binary[len(binary) - i], 2) >= fibonacci_list[i]:
            decimal = (decimal + int(binary[len(binary) - i], 2) - fibonacci_list[i]) * 2 + int(binary[len(binary) - i - 1], 2)
            if decimal >= fibonacci_list[i]:
                decimal -= fibonacci_list[i]
                is_divisible = True
        else:
            decimal = (decimal + int(binary[len(binary) - i], 2)) * 2 + int(binary[len(binary) - i - 1], 2)
    return is_divisible