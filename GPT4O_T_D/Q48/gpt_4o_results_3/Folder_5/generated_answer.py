def return_binary_or_hexa(t):
    if len(t) <= 8:
        return ''
    a, b = (t[2], t[8])
    missing_numbers = {num for num in range(a + 1, b) if num not in t[2:9]}
    sum_missing_numbers = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:]