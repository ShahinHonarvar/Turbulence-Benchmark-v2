def return_binary_or_hexa(t):
    a = t[72]
    b = t[93]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[72:94]]
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]