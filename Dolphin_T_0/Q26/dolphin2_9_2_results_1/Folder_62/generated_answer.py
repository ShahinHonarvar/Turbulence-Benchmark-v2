def sum_in_range(my_list):
    result = 0
    for number in my_list:
        if -28 <= number <= 573:
            result += number
    return result