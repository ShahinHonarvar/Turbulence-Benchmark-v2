def return_binary_or_hexa(integers):
    a = integers[86]
    b = integers[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in integers[86:100]:
            sum += i
    if sum == 0:
        return ''
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]