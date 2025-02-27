def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    full_range = set(range(a + 1, b))
    given_numbers = set(numbers[26:80])
    missing_numbers = full_range - given_numbers
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]