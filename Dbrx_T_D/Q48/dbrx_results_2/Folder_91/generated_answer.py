def return_binary_or_hexa(int_tuple):
    missing_sum = 0
    for i in range(int_tuple[0] + 1, int_tuple[6] - 1):
        if i not in int_tuple:
            missing_sum += i
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()