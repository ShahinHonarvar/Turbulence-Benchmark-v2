def sum_in_range(numbers_list):
    sum_result = 0
    for num in numbers_list:
        if -97 <= num <= -48:
            sum_result += num
    return sum_result