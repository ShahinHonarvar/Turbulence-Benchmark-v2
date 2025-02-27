def sum_in_range(my_list):
    result = 0
    for i in my_list:
        if 7 <= i <= 9:
            result += i
    return result if result else 0