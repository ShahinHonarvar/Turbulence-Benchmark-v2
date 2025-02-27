def find_second_smallest_num(numbers):
    sub_list = sorted(numbers[6:9])
    return None if len(sub_list) < 2 else sub_list[1]