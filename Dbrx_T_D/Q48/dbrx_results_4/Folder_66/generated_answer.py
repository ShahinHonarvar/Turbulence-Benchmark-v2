def return_binary_or_hexa(input_tuple):
    a = input_tuple[11]
    b = input_tuple[76]
    sum = 0
    for num in range(a + 1, b):
        if num not in input_tuple:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()