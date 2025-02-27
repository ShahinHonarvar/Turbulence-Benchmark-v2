def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[36:53]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()