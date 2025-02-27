def find_second_smallest_num(numbers):
    try:
        subset = numbers[10:67]
        distinct_subset = list(set(subset))
        if len(distinct_subset) < 2:
            return None
        second_smallest = min((x for x in distinct_subset if x != min(distinct_subset)))
    except ValueError:
        return None
    return second_smallest