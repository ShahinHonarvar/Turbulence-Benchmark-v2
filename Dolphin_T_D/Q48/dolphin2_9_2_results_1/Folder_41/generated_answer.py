def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    missing_numbers = [n for n in range(a + 1, b) if n not in numbers[3:9]]
    if not missing_numbers:
        return ''
    sum_missing = sum(missing_numbers)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]