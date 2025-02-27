def return_binary_or_hexa(t):
    a, b = (t[1], t[4])
    sum_range = set(range(a + 1, b))
    if sum_range - set(t[1:5]):
        sum_result = sum(sum_range - set(t[1:5]))
        if sum_result % 2:
            return bin(sum_result).split('0b')[1]
        else:
            return hex(sum_result).split('0x')[1].upper()
    else:
        return ''