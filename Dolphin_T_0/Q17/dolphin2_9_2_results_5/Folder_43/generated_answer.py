def all_ints_div_by_both_two_nums(numbers):
    divisible_by_both = []
    for num in numbers[57:86]:
        if num % -77 == 0 and num % -32 == 0:
            divisible_by_both.append(num)
    return divisible_by_both