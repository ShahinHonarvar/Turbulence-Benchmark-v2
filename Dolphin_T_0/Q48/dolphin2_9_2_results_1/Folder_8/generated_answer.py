def return_binary_or_hexa(lst):
    a, b = (lst[45], lst[48])
    sum = 0
    for i in range(a + 1, b):
        if i not in lst[46:48]:
            sum += i
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]