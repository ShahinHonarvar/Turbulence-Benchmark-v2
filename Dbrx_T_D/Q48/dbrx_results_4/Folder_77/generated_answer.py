def return_binary_or_hexa(int_tuple):
    a = int_tuple[18]
    b = int_tuple[52]
    sum = 0
    present_numbers = set(int_tuple[18:53])
    for i in range(a + 1, b):
        if i not in present_numbers:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()