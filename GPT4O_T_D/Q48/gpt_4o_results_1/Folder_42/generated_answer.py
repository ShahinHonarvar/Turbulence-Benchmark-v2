def return_binary_or_hexa(numbers):
    if len(numbers) <= 60:
        return ''
    a = numbers[18]
    b = numbers[60]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[19:60]:
            total += i
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]