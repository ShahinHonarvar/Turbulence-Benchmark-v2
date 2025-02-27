def all_odd_ints_inclusive(lst):
    odd_nums = []
    for num in lst[661:925]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums or []