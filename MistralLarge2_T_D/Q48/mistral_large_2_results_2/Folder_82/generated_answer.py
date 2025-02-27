def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[200])
    present_numbers = set(numbers[20:201])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present_numbers))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()