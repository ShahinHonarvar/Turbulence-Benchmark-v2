def return_binary_or_hexa(lst):
    a = lst[36]
    b = lst[85]
    sum = 0
    for i in range(a + 1, b):
        if i not in lst:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]