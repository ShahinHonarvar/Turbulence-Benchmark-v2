def return_binary_or_hexa(numbers):
    if len(numbers) <= 7:
        return ''
    a, b = (numbers[6], numbers[7])
    if b <= a + 1:
        return ''
    full_set = set(range(a + 1, b))
    missing_numbers = full_set - set(numbers[6:8])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:].upper()