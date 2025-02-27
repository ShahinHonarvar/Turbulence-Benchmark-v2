def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    missing_sum = sum([num for num in range(a + 1, b) if num not in numbers[90:201]])
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()