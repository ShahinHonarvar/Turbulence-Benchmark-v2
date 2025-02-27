def return_binary_or_hexa(t):
    a = t[56]
    b = t[88]
    not_in_tuple = [i for i in range(a + 1, b) if i not in t[57:88]]
    total_sum = sum(not_in_tuple)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:].upper()
    else:
        return bin(total_sum)[2:]