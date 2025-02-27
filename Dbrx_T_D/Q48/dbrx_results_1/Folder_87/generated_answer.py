def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[43]
    sum = 0
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in input_tuple[20:44]:
            sum += i
            missing_numbers.append(i)
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()