def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    missing_sum = 0
    complete = True
    all_numbers = set(range(a + 1, b))
    for number in all_numbers:
        if number not in t[58:84]:
            missing_sum += number
            complete = False
    if complete:
        return ''
    if missing_sum % 2 == 1:
        return format(missing_sum, 'b')
    else:
        return format(missing_sum, 'x')