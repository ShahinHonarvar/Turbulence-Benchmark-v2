def return_binary_or_hexa(tup):
    a = tup[0]
    b = tup[4]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in tup:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]