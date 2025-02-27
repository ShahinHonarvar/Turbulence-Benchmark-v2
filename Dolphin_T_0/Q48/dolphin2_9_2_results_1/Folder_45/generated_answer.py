def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    not_in_range = [x for x in range(a + 1, b) if x not in numbers]
    if len(not_in_range) == 0:
        return ''
    sum_not_in_range = sum(not_in_range)
    if sum_not_in_range % 2 == 1:
        return bin(sum_not_in_range)[2:]
    else:
        return hex(sum_not_in_range)[2:]