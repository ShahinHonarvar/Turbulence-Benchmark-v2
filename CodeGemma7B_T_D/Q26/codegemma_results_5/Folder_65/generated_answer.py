def sum_in_range(lst):
    sum_result = 0
    for number in lst:
        if number >= 77 and number <= 84:
            sum_result += number
    return sum_result if sum_result else 0