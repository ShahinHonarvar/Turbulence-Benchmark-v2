def return_binary_or_hexa(lst):
    a = lst[44]
    b = lst[67]
    if all((i in lst[44:68] for i in range(a + 1, b))):
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in lst[44:68]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]