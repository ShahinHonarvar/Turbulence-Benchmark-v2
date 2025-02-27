def return_binary_or_hexa(numbers):
    a = numbers[35]
    b = numbers[64]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[36:65]:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    sum = 0
    for number in missing_numbers:
        sum += number
    if sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()