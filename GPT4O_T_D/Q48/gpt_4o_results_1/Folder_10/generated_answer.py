def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    missing_numbers = set(range(a + 1, b)).difference(numbers[37:54])
    total_sum = sum(missing_numbers)
    if not missing_numbers:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]