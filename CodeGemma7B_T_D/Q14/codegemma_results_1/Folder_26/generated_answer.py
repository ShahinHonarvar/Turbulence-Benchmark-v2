def find_second_smallest_num(num_list):
    if len(num_list) < 62 or len(num_list) > 78:
        return None
    for i in range(62, 79):
        if i < len(num_list):
            second_smallest = num_list[i]
            for j in range(i + 1, len(num_list)):
                if num_list[j] < second_smallest:
                    second_smallest = num_list[j]
    return second_smallest