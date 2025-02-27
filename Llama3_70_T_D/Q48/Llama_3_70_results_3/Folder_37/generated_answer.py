def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[7]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[2:8]]
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    elif total != 0:
        return hex(total)[2:]
    else:
        return ''