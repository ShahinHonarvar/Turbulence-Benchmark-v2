def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[35])
    if a + 1 == b:
        return ''
    missing_data = [x for x in range(a + 1, b) if x not in numbers]
    sum_missing_data = sum(missing_data)
    if sum_missing_data % 2 != 0:
        return bin(sum_missing_data)[2:]
    else:
        return hex(sum_missing_data)[2:]