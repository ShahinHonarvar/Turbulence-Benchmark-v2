def return_binary_or_hexa(my_tuple):
    sum = 0
    comp = set(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in comp:
            sum += i
    return bin(sum)[2:] if sum % 2 == 1 else hex(sum)[2:].upper() if sum % 2 == 0 else ''