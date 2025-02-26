def return_binary_or_hexa(tup):
    a = tup[20]
    b = tup[93]
    subset = set(tup[20:94])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in subset))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()