def sum_in_range(lst):
    sum = 0
    for num in lst:
        if num >= -885 and num <= -817:
            sum += num
    return sum if sum != 0 else 0