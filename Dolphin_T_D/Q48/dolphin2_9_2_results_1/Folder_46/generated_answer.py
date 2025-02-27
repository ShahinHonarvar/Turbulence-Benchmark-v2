def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[79]
    existing_numbers = set(numbers[10:80])
    sum_of_missing = sum(set(range(a + 1, b)) - existing_numbers)
    if sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]