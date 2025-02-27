def return_binary_or_hexa(num_tuple):
    a = num_tuple[2]
    b = num_tuple[5]
    numbers = num_tuple[2:5]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()