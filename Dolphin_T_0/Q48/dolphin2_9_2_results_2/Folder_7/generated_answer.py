def return_binary_or_hexa(lst):
    a = lst[10]
    b = lst[97]
    s = set(lst[10:98])
    sum = 0
    for i in range(a + 1, b):
        if i not in s:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()