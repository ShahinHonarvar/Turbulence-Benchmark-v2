def all_ints_not_div_by_num(lst):
    not_divisible = []
    subsequence = lst[3:9]
    for num in subsequence:
        if num % 6 != 0:
            not_divisible.append(num)
    return not_divisible