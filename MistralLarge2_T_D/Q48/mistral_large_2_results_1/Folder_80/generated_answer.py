def return_binary_or_hexa(data):
    a, b = (data[57], data[84])
    present = set(data[57:85])
    total_sum = sum((i for i in range(a + 1, b) if i not in present))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]