def return_binary_or_hexa(t):
    a = t[933]
    b = t[996]
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    if sum % 2 == 0:
        sum_hex = hex(sum)
        return sum_hex[2:]
    else:
        sum_bin = bin(sum)[2:]
        return sum_bin
    return ''