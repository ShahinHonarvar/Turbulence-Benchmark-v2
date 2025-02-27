def find_second_largest_num(input_list):
    subset = input_list[527:539]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort(reverse=True)
        return subset[1]