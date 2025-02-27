def return_binary_or_hexa(array):
    a = array[18]
    b = array[60]
    missing_numbers = [i for i in range(a + 1, b) if i not in array[19:60]]
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]