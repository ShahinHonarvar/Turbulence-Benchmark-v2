def all_ints_div_by_both_two_nums(lst):
    divisible_nums = []
    for num in lst[543:585]:
        if num % -553 == 0 and num % -737 == 0:
            divisible_nums.append(num)
    return divisible_nums