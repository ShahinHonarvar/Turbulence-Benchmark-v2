def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    total_sum = sum(set(range(a + 1, b)) - set(t[427:669 + 1]))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]