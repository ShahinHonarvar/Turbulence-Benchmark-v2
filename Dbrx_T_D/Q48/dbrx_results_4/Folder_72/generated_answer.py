def return_binary_or_hexa(input_tuple):
    a = input_tuple[13]
    b = input_tuple[70]
    sum = 0
    present_numbers = set(input_tuple[13:71])
    for i in range(a + 1, b):
        if i not in present_numbers:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()