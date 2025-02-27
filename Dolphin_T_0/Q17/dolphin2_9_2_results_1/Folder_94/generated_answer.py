def all_ints_div_by_both_two_nums(arr):
    div_by_both = []
    for num in arr[93:95]:
        if num % -53 == 0 and num % -91 == 0:
            div_by_both.append(num)
    return div_by_both