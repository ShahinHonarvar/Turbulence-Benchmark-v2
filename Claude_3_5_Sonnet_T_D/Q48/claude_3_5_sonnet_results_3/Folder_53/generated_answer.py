def return_binary_or_hexa(tup):
    a = tup[200]
    b = tup[202]
    excluded_set = set(tup[200:203])
    sum_not_present = sum((num for num in range(a + 1, b) if num not in excluded_set))
    if sum_not_present == 0:
        return ''
    elif sum_not_present % 2 == 1:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].rstrip('L')