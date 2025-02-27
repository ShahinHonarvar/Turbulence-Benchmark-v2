def return_binary_or_hexa(tuple_nums):
    a = tuple_nums[37]
    b = tuple_nums[43]
    missing_nums = set(range(a + 1, b))
    present_nums = set(tuple_nums[37 + 1:43])
    missing_sum = sum(missing_nums - present_nums)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]