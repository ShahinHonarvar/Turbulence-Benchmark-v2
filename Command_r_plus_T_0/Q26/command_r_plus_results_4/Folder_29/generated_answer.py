def sum_in_range(numbers_list):
    sum_result = 0
    for num in numbers_list:
        if 18 <= num <= 60:
            sum_result += num
    return sum_result