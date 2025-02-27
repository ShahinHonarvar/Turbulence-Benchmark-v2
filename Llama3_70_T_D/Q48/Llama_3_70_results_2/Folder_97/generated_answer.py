def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    present_numbers = set(numbers[34:70])
    missing_numbers = [i for i in range(a + 1, b) if i not in present_numbers]
    total = sum(missing_numbers)
    if total == 0:
        return ''
    elif total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]