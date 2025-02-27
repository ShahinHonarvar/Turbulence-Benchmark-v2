def return_binary_or_hexa(input_tuple):
    a = input_tuple[33]
    b = input_tuple[78]
    sum = 0
    for number in range(a + 1, b + 1):
        if number not in input_tuple[33:79]:
            sum += number
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]