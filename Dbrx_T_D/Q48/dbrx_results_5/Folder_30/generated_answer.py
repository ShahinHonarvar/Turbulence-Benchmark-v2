def return_binary_or_hexa(int_tuple):
    a = int_tuple[22]
    b = int_tuple[24]
    sum = 0
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in int_tuple[22:25]:
            sum += i
            missing_numbers.append(i)
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]