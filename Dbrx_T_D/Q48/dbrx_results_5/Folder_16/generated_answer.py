def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    present_numbers = set(numbers[90:98])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()