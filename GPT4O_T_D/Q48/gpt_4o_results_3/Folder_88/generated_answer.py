def return_binary_or_hexa(numbers):
    if len(numbers) < 10:
        return ''
    a = numbers[3]
    b = numbers[9]
    if b - a <= 1:
        return ''
    numbers_set = set(numbers[4:9])
    total = sum((n for n in range(a + 1, b) if n not in numbers_set))
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]