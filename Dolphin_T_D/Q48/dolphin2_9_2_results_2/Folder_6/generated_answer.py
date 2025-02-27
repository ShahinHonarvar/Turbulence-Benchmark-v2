def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    present = set(numbers[21:93])
    missing = [i for i in range(a + 1, b) if i not in present]
    if not missing:
        return ''
    sum_missing = sum(missing)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()