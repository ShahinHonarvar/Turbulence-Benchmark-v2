def find_second_largest_num(numbers):
    subset = numbers[40:81]
    subset.sort(reverse=True)
    if len(subset) >= 2:
        return subset[1]
    else:
        return None