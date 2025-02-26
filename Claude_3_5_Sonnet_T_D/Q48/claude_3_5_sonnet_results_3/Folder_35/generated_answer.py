def return_binary_or_hexa(t):
    a = t[77]
    b = t[84]
    excluded_numbers = set(t[77:85])
    sum_range = sum((num for num in range(a + 1, b) if num not in excluded_numbers))
    if sum_range == 0:
        return ''
    elif sum_range % 2 != 0:
        return bin(sum_range)[2:]
    else:
        return hex(sum_range)[2:].rstrip('L')