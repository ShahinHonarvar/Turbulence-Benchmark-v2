def return_binary_or_hexa(t):
    a = t[33]
    b = t[78]
    existing_numbers = set(t[33:79])
    sum_missing = sum((num for num in range(a + 1, b) if num not in existing_numbers))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]