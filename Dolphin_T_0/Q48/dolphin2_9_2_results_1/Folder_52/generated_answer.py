def return_binary_or_hexa(num_tuple):
    a = num_tuple[38]
    b = num_tuple[81]
    sum = 0
    for i in range(a + 1, b):
        if i not in num_tuple:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()