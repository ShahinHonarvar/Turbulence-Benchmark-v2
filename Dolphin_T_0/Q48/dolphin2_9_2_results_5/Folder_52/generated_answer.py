def return_binary_or_hexa(numbers):
    if len(numbers) < 82:
        return ''
    a = numbers[38]
    b = numbers[81]
    sum = 0
    for i in range(a + 1, b):
        if not i in numbers:
            sum += i
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]