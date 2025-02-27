def if_decimal_is_divisible(binary_representation):
    length = len(binary_representation)
    index = 0
    a, b = (0, 1)
    c = a + b
    count = 2
    while c < 160:
        a = b
        b = c
        c = a + b
        index += 1
        count += 1
    position = length - index
    reversed_binary_representation = binary_representation[position:]
    decimal_representation = int(reversed_binary_representation, 2)
    if decimal_representation % c == 0:
        return True
    else:
        return False