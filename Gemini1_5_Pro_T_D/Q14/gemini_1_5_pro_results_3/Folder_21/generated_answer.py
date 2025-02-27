def find_second_smallest_num(numbers):
    if len(numbers) < 924:
        return None
    sub_list = numbers[661:925]
    if len(set(sub_list)) < 2:
        return None
    sorted_sub_list = sorted(sub_list)
    return sorted_sub_list[1]