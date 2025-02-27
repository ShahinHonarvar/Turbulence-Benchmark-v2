def return_binary_or_hexa(num_tuple):
    a = num_tuple[57]
    b = num_tuple[84]
    sum = 0
    for num in range(a + 1, b):
        if num not in num_tuple:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]