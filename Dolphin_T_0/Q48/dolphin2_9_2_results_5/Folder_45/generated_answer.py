def return_binary_or_hexa(t):
    a = t[30]
    b = t[200]
    if all((a + 1 <= x <= b - 1 for x in t[31:200])):
        return ''
    sum = 0
    for i in range(a + 1, b):
        if i not in t[31:200]:
            sum += i
    return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:].upper()