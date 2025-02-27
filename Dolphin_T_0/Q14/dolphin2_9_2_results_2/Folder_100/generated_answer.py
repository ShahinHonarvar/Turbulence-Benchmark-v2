def find_second_smallest_num(numbers):
    sublist = numbers[43:52]
    distinct_sublist = list(set(sublist))
    if len(distinct_sublist) < 2:
        return None
    else:
        return sorted(distinct_sublist)[1]