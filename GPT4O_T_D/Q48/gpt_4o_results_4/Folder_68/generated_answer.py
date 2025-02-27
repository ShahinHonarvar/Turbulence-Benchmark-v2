def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    required_set = set(range(a + 1, b))
    given_set = set(numbers[0:10])
    missing_numbers = required_set - given_set
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]