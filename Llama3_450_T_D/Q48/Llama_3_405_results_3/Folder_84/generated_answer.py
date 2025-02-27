def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[33:44]]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]