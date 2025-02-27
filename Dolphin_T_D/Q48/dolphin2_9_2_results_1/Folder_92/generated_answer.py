def return_binary_or_hexa(stored_tuple):
    a = stored_tuple[0]
    b = stored_tuple[2]
    sum = 0
    for i in stored_tuple:
        if i > a and i < b:
            sum += i
    if b - a > len(stored_tuple) - 1:
        for i in range(a + 1, b):
            if i not in stored_tuple:
                sum += i
    if sum % 2 == 0:
        if sum != 0:
            return hex(sum)[2:]
        else:
            return ''
    else:
        return bin(sum)[2:]