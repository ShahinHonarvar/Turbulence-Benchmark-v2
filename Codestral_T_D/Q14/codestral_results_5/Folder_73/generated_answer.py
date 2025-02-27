def find_second_smallest_num(numbers):
    subset = numbers[59:98]
    if len(subset) < 2:
        return None
    else:
        smallest = min(subset)
        subset.remove(smallest)
        second_smallest = min(subset)
        return second_smallest