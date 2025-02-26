def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    excluded = set(tup[1:5])
    sum_range = sum((num for num in range(a + 1, b) if num not in excluded))
    if sum_range == 0:
        return ''
    elif sum_range % 2 != 0:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:]