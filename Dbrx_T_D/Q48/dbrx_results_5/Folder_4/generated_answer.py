def return_binary_or_hexa(input_tuple):
    a = input_tuple[49]
    b = input_tuple[74]
    sum = 0
    for i in range(max(a + 1, 50), min(b - 1, 73) + 1):
        if input_tuple.count(i) == 1:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()