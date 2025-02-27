def all_ints_div_by_both_two_nums(lst_nums):
    all_the_numbers = lst_nums[44:60]
    li = list()
    for i in all_the_numbers:
        if i % 39 == 0 and i % 15 == 0:
            li.append(i)
    return li if len(li) else []