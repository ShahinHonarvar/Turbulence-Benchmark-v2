def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[20], num_tuple[200])
    total_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[20:200]))
    return bin(total_sum)[2:] if total_sum & 1 else hex(total_sum)[2:]