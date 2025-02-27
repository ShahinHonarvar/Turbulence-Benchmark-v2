def return_binary_or_hexa(numbers):
    a, b = (numbers[1], numbers[7])
    sum_of_missing = sum((i for i in range(a + 1, b) if i not in numbers[1:7]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()