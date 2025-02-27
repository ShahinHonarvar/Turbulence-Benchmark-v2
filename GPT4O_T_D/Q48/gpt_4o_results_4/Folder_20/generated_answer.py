def return_binary_or_hexa(numbers):
    if len(numbers) <= 96:
        return ''
    a = numbers[27]
    b = numbers[96]
    missing_numbers = set(range(a + 1, b))
    present_numbers = set(numbers[28:96])
    absent_numbers = missing_numbers - present_numbers
    total_sum = sum(absent_numbers)
    if len(absent_numbers) == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]