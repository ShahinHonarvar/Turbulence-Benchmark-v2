def return_binary_or_hexa(lst):
    a = lst[6]
    b = lst[7]
    sum = 0
    for i in range(a + 1, b):
        if i not in lst[6:8]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]