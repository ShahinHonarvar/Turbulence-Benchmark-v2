def return_binary_or_hexa(numbers):
    if len(numbers) < 45:
        return ''
    a = numbers[32]
    b = numbers[44]
    nums_in_range = set(numbers[33:44])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_in_range))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]