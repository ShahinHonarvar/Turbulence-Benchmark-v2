def all_ints_div_by_both_two_nums(lst):
    two_nums = [82, 90]
    result = []
    for i in range(len(lst)):
        if i >= 41 and i <= 56:
            for num in two_nums:
                if lst[i] % num != 0:
                    break
                if num == two_nums[-1]:
                    result.append(lst[i])
    return result