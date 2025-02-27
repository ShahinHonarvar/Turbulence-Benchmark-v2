def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[44:92]))
    if sum_missing == 0:
        return ''
    return bin(sum_missing)[2:] if sum_missing % 2 == 1 else hex(sum_missing)[2:]