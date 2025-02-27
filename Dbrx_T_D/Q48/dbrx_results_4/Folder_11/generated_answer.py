def return_binary_or_hexa(t):
    a, b = (t[48], t[76])
    missing_numbers = set(range(a + 1, b))
    for num in t[48:77]:
        if num in missing_numbers:
            missing_numbers.remove(num)
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return format(sum_of_missing, 'b')
    else:
        return format(sum_of_missing, 'x').upper()