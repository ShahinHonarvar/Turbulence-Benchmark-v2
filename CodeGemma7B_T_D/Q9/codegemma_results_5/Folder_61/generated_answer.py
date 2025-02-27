def all_odd_ints_inclusive(lst):
    odd_nums = []
    if len(lst) > 7:
        for num in lst[0:8]:
            if num % 2 != 0:
                odd_nums.append(num)
    return odd_nums