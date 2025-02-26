def return_binary_or_hexa(tup):
    a = tup[38]
    b = tup[52]
    missing_numbers = []
    for num in range(a + 1, b):
        if num not in tup[38:53]:
            missing_numbers.append(num)
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]