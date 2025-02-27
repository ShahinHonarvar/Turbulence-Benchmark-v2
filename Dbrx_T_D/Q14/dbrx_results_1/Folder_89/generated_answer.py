def find_second_smallest_num(numbers):
    start_index = 62
    end_index = 63
    sublist = numbers[start_index:end_index + 1]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    return second_smallest