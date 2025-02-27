def return_binary_or_hexa(t):
    a, b = (t[60], t[200])
    present_numbers = set(t[60:201])
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, 'b')
    else:
        return format(sum_of_missing_numbers, 'x')