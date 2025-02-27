def if_decimal_is_divisible(binary_string):
    index, exact_binary, multiplier = (0, '', 1)
    for digit in binary_string[::-1]:
        exact_binary = exact_binary + str(int(digit) * multiplier % 59)
        multiplier = multiplier * 2 % 59
        if index == len(binary_string) - 1:
            divisible = int(exact_binary, 2) % 59 == 0
            return divisible
        index += 1