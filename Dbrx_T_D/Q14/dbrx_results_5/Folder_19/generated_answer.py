def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[4:9]
    if len(sublist) < 2:
        return None
    first, second = (min(sublist[:2]), max(sublist[:2]))
    for num in sublist[2:]:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    if second == max(sublist):
        return None
    else:
        return second