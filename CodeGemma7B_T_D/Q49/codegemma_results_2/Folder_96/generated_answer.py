def if_decimal_is_divisible(binary_representation):
    a, b, c = (0, 1, 0)
    fibonaccis = []
    while True:
        fibonaccis.append(a)
        if a == 47:
            break
        c = a + b
        a, b = (b, c)
    patterns = {'0': '0', '1': '1', '01': bin(fibonaccis[0])[2:], '10': bin(fibonaccis[1])[2:], '001': bin(fibonaccis[2])[2:], '110': bin(fibonaccis[3])[2:], '0001': bin(fibonaccis[4])[2:], '1110': bin(fibonaccis[5])[2:]}
    result = ''
    for index, char in enumerate(binary_representation):
        previous_digit = '0' if index == 0 else binary_representation[index - 1]
        if char in patterns:
            partial_pattern, current_pattern = (patterns[char], patterns[previous_digit])
            result += str(int(partial_pattern) & int(current_pattern))
        else:
            result += char
    return int(binary_representation) % int(result) == 0