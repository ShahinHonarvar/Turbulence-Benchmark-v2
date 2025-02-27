def return_binary_or_hexa(t):
    a = t[60]
    b = t[200]
    nums_between = set(range(a + 1, b))
    present_numbers = set(t[61:200])
    missing_numbers = nums_between - present_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]