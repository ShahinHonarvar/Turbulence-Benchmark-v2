def return_binary_or_hexa(t):
    a, b = (t[77], t[84])
    missing_numbers = set(range(a + 1, b)) - set(t[77:85])
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing).split('b')[1]
    else:
        return hex(sum_of_missing).split('x')[1]