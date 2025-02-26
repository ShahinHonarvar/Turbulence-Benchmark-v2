def all_ints_div_by_both_two_nums(numbers):
    divisible_numbers = []
    for num in numbers[828:933]:
        if num % -649 == 0 and num % -461 == 0:
            divisible_numbers.append(num)
    return divisible_numbers