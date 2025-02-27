def all_ints_div_by_both_two_nums(numbers):
    divisible_by_both = []
    for num in numbers[543:585]:
        if num % -553 == 0 and num % -737 == 0:
            divisible_by_both.append(num)
    return divisible_by_both