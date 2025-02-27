def return_binary_or_hexa(numbers):
    a, b = (numbers[34], numbers[69])
    subset = set(numbers[34 + 1:69])
    missing = set(range(a + 1, b)) - subset
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    elif sum_missing > 0:
        return hex(sum_missing)[2:]
    else:
        return ''