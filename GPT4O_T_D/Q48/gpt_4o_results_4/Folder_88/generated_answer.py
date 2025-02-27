def return_binary_or_hexa(numbers):
    if len(numbers) < 10:
        return ''
    a, b = (numbers[3], numbers[9])
    missing_numbers = {x for x in range(a + 1, b)} - set(numbers[4:9])
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]