def sum_ints_div_by_either_nums(numbers):
    sum_val = 0
    for i in numbers[80:201]:
        if i % 10 == 0 or i % 1000 == 0:
            sum_val += i
    return sum_val