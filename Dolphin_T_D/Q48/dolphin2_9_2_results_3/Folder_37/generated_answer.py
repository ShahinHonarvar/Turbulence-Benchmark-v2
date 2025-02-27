def return_binary_or_hexa(t):
    a = t[2]
    b = t[7]
    missing_numbers = [i for i in range(a + 1, b) if i not in t[2:8]]
    if not missing_numbers:
        return ''
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 1:
        return bin(sum_missing_numbers)[2:]
    else:
        return hex(sum_missing_numbers)[2:].upper()