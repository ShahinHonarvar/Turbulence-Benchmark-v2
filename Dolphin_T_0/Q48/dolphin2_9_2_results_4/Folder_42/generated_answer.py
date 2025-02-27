def return_binary_or_hexa(lst):
    a = lst[18]
    b = lst[60]
    missing_numbers = [num for num in range(a + 1, b) if num not in lst[18:61]]
    if not missing_numbers:
        return ''
    sum = 0
    for num in missing_numbers:
        sum += num
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]