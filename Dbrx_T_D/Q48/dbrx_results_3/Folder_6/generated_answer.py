def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    sum = 0
    present_numbers = set(numbers[20:94])
    for i in range(a + 1, b):
        if i not in present_numbers:
            sum += i
    if sum % 2:
        return format(sum, '08b')
    else:
        return format(sum, 'x')