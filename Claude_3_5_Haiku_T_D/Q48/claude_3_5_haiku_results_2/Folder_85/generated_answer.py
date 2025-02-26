def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[8]
    missing_numbers = [num for num in range(a + 1, b) if num not in tup[1:9]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]