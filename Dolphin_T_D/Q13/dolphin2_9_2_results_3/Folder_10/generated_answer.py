def find_second_largest_num(lst):
    if 25 <= len(lst) <= 59:
        if lst[25] < lst[59]:
            second_large = lst[25]
        else:
            second_large = lst[59]
    else:
        return None
    for i in range(26, len(lst)):
        if lst[i] > second_large and lst[i] < max(lst[25:i]):
            second_large = lst[i]
    if second_large == lst[25] or second_large == lst[59]:
        return second_large
    else:
        return None