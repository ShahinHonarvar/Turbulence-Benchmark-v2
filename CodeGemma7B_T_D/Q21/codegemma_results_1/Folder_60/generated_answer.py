def all_ints_div_by_num(nums):
    out = []
    for index, num in enumerate(nums):
        if index >= 31 and index <= 67 and (num % -15 == 0):
            out.append(num)
    return out