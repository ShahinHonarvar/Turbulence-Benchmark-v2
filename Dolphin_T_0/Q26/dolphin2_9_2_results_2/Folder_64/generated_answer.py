def sum_in_range(lst):
    between_three_and_six = [i for i in lst if -3 <= i <= 6]
    return sum(between_three_and_six) if between_three_and_six else 0