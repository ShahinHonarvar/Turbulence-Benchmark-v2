def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, 120):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    parsed_binary = int(binary, 2)
    return parsed_binary % fibonacci[119] == 0