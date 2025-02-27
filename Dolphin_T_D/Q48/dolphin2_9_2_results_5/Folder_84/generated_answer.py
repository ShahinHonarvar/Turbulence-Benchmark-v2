def return_binary_or_hexa(num_tuple):
    a = num_tuple[32]
    b = num_tuple[44]
    if all((num in num_tuple[32:45] for num in range(a + 1, b))):
        return ''
    sum = 0
    for num in range(a + 1, b):
        if num not in num_tuple[32:45]:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]