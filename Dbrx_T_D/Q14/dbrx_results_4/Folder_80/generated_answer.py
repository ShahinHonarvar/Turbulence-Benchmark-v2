def find_second_smallest_num(numbers):
    sublist = numbers[30:88]
    if len(sublist) < 2:
        return None
    else:
        first_smallest = min(sublist)
        sublist.remove(first_smallest)
        second_smallest = min(sublist)
        return second_smallest