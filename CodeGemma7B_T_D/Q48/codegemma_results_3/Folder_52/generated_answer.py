def return_binary_or_hexa(int_tuple):
    final_sum = 0
    for i in range(39, 82):
        if i not in int_tuple:
            final_sum += i
    if final_sum % 2 == 1:
        return bin(final_sum)[2:]
    else:
        return hex(final_sum)[2:].upper()