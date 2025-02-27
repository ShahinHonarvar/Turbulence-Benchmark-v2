def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    existing_numbers = set(numbers[91:97])
    total_sum = sum((x for x in range(a + 1, b) if x not in existing_numbers))
    if not total_sum:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]