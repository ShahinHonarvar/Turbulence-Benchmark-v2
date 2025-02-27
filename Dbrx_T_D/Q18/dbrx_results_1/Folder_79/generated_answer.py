def sum_ints_div_by_either_nums(numbers):
    subrange = numbers[8:10]
    sum = 0
    for num in subrange:
        if num % -3 == 0 or num % 6 == 0:
            sum += num
    return sum