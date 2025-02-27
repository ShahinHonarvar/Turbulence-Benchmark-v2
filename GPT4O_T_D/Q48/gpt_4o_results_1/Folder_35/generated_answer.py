def return_binary_or_hexa(numbers):
    a, b = (numbers[77], numbers[84])
    range_nums = set(range(a + 1, b))
    missing_nums = range_nums - set(numbers[78:84])
    sum_missing = sum(missing_nums)
    if missing_nums:
        if sum_missing % 2:
            return bin(sum_missing)[2:]
        else:
            return hex(sum_missing)[2:]
    return ''