def find_second_smallest_num(numbers):
    if len(numbers) < 23:
        return None
    sublist = numbers[23:24]
    if len(sublist) == 1:
        smallest_num = sublist[0]
        second_smallest_num = None
    else:
        smallest_num = min(sublist[0], sublist[1])
        second_smallest_num = max(sublist[0], sublist[1])
    if len(sublist) == 1 and (not second_smallest_num):
        return None
    for num in numbers:
        if num < smallest_num and num != smallest_num:
            second_smallest_num, smallest_num = (smallest_num, num)
        elif num > smallest_num and (not second_smallest_num or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num