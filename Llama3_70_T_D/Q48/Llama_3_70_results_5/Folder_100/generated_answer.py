def return_binary_or_hexa(num_tuple):
    a = num_tuple[44]
    b = num_tuple[78]
    num_set = set(num_tuple[44:79])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    return bin(total_sum)[2:] if total_sum % 2 != 0 else hex(total_sum)[2:]