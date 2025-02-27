def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[68:100]]
    total = sum(missing_numbers)
    if not total:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]