def all_ints_div_by_both_two_nums(numbers):
    range_numbers = numbers[543:585]
    divisible_numbers = [num for num in range_numbers if num % -553 == 0 and num % -737 == 0]
    return divisible_numbers