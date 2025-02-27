def return_binary_or_hexa(numbers):
    if len(numbers) <= 9:
        return ''
    a = numbers[6]
    b = numbers[9]
    numbers_in_range = set(numbers[7:9])
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers_in_range))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]