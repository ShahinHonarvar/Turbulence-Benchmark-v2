def return_binary_or_hexa(input_tuple):
    a = input_tuple[86]
    b = input_tuple[89]
    sum = 0
    for num in range(a + 1, b):
        if num not in input_tuple[a + 1:b]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()