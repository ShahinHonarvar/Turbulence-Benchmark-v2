def return_binary_or_hexa(numbers):
    a, b = (numbers[60], numbers[200])
    sum_missing = sum((x for x in range(a + 1, b) if x not in numbers[60:201]))
    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]