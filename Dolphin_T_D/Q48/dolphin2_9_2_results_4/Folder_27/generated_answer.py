def return_binary_or_hexa(array):
    a = array[86]
    b = array[89]
    if a + 1 == b:
        return ''
    total = sum((i for i in range(a + 1, b) if i not in array[86:90]))
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]