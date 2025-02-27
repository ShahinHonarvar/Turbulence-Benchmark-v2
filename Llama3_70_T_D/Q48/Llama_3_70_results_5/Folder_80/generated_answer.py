def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[58:84]]
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total > 0:
        return hex(total)[2:]
    else:
        return ''