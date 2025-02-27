def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    sublist = numbers[33:37]
    if len(sublist) < 2:
        return None
    smallest_num = min(sublist)
    second_smallest_num = None
    for num in sublist:
        if num > smallest_num and (second_smallest_num is None or num < second_smallest_num):
            second_smallest_num = num
    return second_smallest_num