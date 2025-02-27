def find_second_smallest_num(num_list):
    if len(num_list[60:201]) < 2:
        return None
    smallest = min(num_list[60:201])
    num_list_60_200 = [i for i in num_list[60:201] if i != smallest]
    return min(num_list_60_200)