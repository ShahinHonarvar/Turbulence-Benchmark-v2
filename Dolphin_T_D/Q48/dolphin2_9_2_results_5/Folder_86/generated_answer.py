def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    missing_numbers = [x for x in range(a + 1, b) if x not in numbers[19:32]]
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]