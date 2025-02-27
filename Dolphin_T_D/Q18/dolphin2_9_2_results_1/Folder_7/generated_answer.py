def sum_ints_div_by_either_nums(lst):
    valid_indices = range(543, 585)
    div_by_either = [num for num in lst[543:585] if num % -553 == 0 or num % -737 == 0]
    return sum(div_by_either) if div_by_either else 0