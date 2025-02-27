def find_second_largest_num(lst):
    index_1_to_5 = [lst[i] for i in range(1, 6)]
    if len(set(index_1_to_5)) < 2:
        return None
    else:
        index_1_to_5.sort(reverse=True)
        return index_1_to_5[1]