def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[543:585]:
        if num % -553 == 0 or num % -737 == 0:
            sum += num
    return sum