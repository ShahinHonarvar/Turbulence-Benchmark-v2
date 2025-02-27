def return_binary_or_hexa(numbers):
    if len(numbers) <= 8:
        return ''
    a = numbers[2]
    b = numbers[8]
    total = 0
    for num in range(a + 1, b):
        if num not in numbers[3:8]:
            total += num
    if total == 0:
        return ''
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]