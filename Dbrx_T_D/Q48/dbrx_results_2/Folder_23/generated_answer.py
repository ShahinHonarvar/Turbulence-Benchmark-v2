def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[36]
    sum_of_missing = sum(set(range(a + 1, b)) - set(numbers[20:37]))
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:].upper()