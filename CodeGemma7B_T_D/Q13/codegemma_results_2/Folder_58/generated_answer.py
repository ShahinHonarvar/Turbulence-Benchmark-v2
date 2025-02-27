def find_second_largest_num(random_list):
    sorted_list = sorted(random_list)
    second_largest = sorted_list[-2]
    second_largest = second_largest if second_largest >= sorted_list[208] and second_largest <= sorted_list[556] else 'None'
    return second_largest