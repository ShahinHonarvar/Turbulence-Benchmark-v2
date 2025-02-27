def return_binary_or_hexa(numbers):
    a, b = (numbers[69], numbers[97])
    missing = [i for i in range(a + 1, b) if i not in numbers[69:98]]
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]