def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[12:76]]
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]