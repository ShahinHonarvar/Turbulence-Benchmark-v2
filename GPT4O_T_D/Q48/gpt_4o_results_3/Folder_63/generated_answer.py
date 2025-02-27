def return_binary_or_hexa(numbers):
    a, b = (numbers[81], numbers[86])
    sum_non_present = sum((i for i in range(a + 1, b) if i not in set(numbers[81:87])))
    if sum_non_present == 0:
        return ''
    if sum_non_present % 2:
        return bin(sum_non_present)[2:]
    else:
        return hex(sum_non_present)[2:]