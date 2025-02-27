def return_binary_or_hexa(numbers):
    a, b = (numbers[90], numbers[200])
    missing_numbers = []
    for i in range(a + 1, b):
        if i not in numbers:
            missing_numbers.append(i)
    if not missing_numbers:
        return ''
    sum = 0
    for num in missing_numbers:
        sum += num
    return bin(sum)[2:] if sum % 2 != 0 else hex(sum)[2:]