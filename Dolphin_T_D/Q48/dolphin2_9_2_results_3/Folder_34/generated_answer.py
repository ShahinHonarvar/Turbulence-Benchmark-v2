def return_binary_or_hexa(numbers):
    a = numbers[60]
    b = numbers[200]
    all_nums = set(range(a + 1, b))
    not_in_tuple = all_nums.difference(set(numbers[60:201]))
    sum_of_not_in_tuple = sum(not_in_tuple)
    if len(not_in_tuple) == 0:
        return ''
    elif sum_of_not_in_tuple % 2 == 0:
        return hex(sum_of_not_in_tuple)[2:]
    else:
        return bin(sum_of_not_in_tuple)[2:]