def return_binary_or_hexa(num_tuple):
    a = num_tuple[1]
    b = num_tuple[7]
    num_set = set(num_tuple[1:8])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]