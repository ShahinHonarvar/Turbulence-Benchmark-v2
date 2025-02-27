def return_binary_or_hexa(integers):
    a = integers[37]
    b = integers[43]
    sum = 0
    for i in range(a + 1, b):
        if i not in integers[37:44]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]