def sum_in_range(numbers_list):
    sum_result = 0
    for num in numbers_list:
        if -91 <= num <= -61:
            sum_result += num
    return sum_result