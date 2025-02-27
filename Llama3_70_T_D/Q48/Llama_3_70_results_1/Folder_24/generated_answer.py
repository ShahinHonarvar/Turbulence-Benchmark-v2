def return_binary_or_hexa(num_tuple):
    a = num_tuple[13]
    b = num_tuple[91]
    missing_numbers = [i for i in range(a + 1, b) if i not in num_tuple[13:92]]
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]