def return_binary_or_hexa(tup):
    a = tup[275]
    b = tup[871]
    all_nums_included = True
    sum = 0
    for num in range(a + 1, b):
        if num not in tup:
            all_nums_included = False
            sum += num
    if all_nums_included:
        return ''
    elif sum % 2 == 0:
        return hex(sum)[2:].upper()
    else:
        return bin(sum)[2:]