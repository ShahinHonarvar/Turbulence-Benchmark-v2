def return_binary_or_hexa(number_tuple):
    a = number_tuple[13]
    b = number_tuple[70]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in number_tuple[13:71]:
            total_sum += i
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]