def return_binary_or_hexa(t):
    a = t[86]
    b = t[90]
    existing_numbers = set(t[87:90])
    total_sum = 0
    for num in range(a + 1, b):
        if num not in existing_numbers:
            total_sum += num
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return format(total_sum, 'b')
    else:
        return format(total_sum, 'x')