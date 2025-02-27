def if_decimal_is_divisible(binary_string):
    fibnumbers = [0, 1]
    for i in range(2, 170):
        fibnumbers.append(fibnumbers[i - 1] + fibnumbers[i - 2])
    was_number_set = False
    for bit in binary_string:
        if bit == '1':
            was_number_set = True
    if was_number_set:
        decimal_number = int(binary_string, 2)
        return decimal_number % fibnumbers[167] == 0
    else:
        return False