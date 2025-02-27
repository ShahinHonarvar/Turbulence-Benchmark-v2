def find_second_smallest_num(numbers):
    if len(numbers) < 9 or len(numbers) > 10:
        return None
    sublist = numbers[6:9]
    if len(sublist) < 2:
        return None
    first_smallest = min(sublist)
    sublist.remove(first_smallest)
    second_smallest = min(sublist)
    if first_smallest < second_smallest:
        return second_smallest
    else:
        return first_smallest