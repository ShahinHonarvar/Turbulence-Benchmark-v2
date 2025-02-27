def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers]
    if len(missing_numbers) == 0:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:].upper()
    else:
        return bin(sum_missing)[2:]