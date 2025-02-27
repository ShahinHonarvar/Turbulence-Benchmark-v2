def return_binary_or_hexa(num_tuple):
    a = num_tuple[43]
    b = num_tuple[70]
    num_set = set(num_tuple[43:71])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    elif total_sum != 0:
        return hex(total_sum)[2:]
    else:
        return ''