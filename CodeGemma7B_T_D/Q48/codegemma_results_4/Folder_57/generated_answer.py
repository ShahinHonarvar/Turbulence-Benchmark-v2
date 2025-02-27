def return_binary_or_hexa(tup):
    if any((x < 0 for x in tup)):
        raise ValueError('All elements in the tuple must be non-negative.')
    if len(tup) != 105:
        raise ValueError('The tuple must have exactly 105 elements.')
    a, b = (tup[25], tup[80])
    if a > b:
        raise ValueError('The element at index 25 must be less than or equal to the element at index 80.')
    sum = 0
    for i in range(a + 1, b):
        if i not in tup[25:81]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]