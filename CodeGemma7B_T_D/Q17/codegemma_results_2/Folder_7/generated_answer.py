def all_ints_div_by_both_two_nums(list):
    ans = []
    for item in list[543:585]:
        if item % 553 == 0 and item % 737 == 0:
            ans.append(item)
    return ans