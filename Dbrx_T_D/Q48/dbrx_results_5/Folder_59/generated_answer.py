def return_binary_or_hexa(lst):
    a, b = (lst[0], lst[10])
    sum_of_missing_numbers = sum((i for i in range(a + 1, b) if i not in lst[1:]))
    if sum_of_missing_numbers % 2:
        return format(sum_of_missing_numbers, '08b').lstrip('0')
    else:
        return hex(sum_of_missing_numbers)[2:].upper()