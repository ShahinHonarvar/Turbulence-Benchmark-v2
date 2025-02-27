def find_second_smallest_num(input_list):
    subset = input_list[62:79]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    else:
        second_smallest = sorted_subset[1]
        return second_smallest