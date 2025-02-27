def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]