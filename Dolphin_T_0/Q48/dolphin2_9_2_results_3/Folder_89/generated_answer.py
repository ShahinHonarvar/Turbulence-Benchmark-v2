def return_binary_or_hexa(passed_tuple):
    a = passed_tuple[55]
    b = passed_tuple[84]
    if a + 1 >= b - 1:
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in passed_tuple[56:84]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]