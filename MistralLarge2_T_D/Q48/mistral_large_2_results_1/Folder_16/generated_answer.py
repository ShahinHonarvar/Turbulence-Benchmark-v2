def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    subset = numbers[90:98]
    missing_numbers = [x for x in range(a + 1, b) if x not in subset]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]