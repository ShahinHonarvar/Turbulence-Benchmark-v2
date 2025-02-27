def find_second_largest_num(num_list):
    second_largest = None
    for num in num_list[5:8]:
        if num > second_largest or second_largest is None:
            second_largest = num
    return second_largest