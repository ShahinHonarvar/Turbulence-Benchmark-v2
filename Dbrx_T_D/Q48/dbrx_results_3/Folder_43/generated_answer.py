def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers[10:29]:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    else:
        sum_missing = sum(missing_numbers)
    if sum_missing % 2 != 0:
        return bin(sum_missing).replace('0b', '')
    else:
        return hex(sum_missing).replace('0x', '').upper()