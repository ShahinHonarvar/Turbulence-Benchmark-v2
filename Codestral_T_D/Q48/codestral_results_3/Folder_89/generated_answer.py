def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    missing_numbers = set(range(a + 1, b))
    existing_numbers = set(numbers[55 + 1:84])
    missing_numbers.difference_update(existing_numbers)
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]