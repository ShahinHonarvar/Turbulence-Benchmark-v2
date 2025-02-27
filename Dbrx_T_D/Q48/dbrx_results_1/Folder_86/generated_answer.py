def return_binary_or_hexa(int_tuple):
    a = int_tuple[19]
    b = int_tuple[32]
    sum = 0
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in int_tuple[19:33]:
            sum += i
            missing_numbers.append(i)
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()