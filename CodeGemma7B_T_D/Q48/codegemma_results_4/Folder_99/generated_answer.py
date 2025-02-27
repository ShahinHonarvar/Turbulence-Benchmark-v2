def return_binary_or_hexa(array):
    a = array[427]
    b = array[669]
    total = 0
    for num in range(a + 1, b):
        if num not in array:
            total += num
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper() if total < 8 else hex(total)[2:]