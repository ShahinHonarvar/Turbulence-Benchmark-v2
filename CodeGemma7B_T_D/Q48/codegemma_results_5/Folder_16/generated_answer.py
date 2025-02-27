def return_binary_or_hexa(my_tuple):
    a = my_tuple[90]
    b = my_tuple[97]
    sum = 0
    for num in range(a + 1, b):
        if num not in my_tuple[90:97 + 1]:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()