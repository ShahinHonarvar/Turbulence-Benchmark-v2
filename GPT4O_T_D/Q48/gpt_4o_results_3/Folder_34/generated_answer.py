def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    numbers_in_range = set(numbers[61:200])
    total_sum = sum((num for num in range(a + 1, b) if num not in numbers_in_range))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]