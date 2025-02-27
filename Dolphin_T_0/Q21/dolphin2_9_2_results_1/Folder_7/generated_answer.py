def all_ints_div_by_num(numbers):
    divisible_numbers = []
    for num in numbers[315:353]:
        if num % -858 == 0:
            divisible_numbers.append(num)
    return divisible_numbers