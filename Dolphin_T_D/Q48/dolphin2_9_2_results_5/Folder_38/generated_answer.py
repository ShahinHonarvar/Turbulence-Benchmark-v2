def return_binary_or_hexa(int_list):
    a = int_list[36]
    b = int_list[85]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in int_list[37:85]:
            missing_sum += i
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]