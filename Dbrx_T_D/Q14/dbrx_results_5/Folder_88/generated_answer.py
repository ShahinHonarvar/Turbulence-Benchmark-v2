def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers) < 9:
        return None
    sub_list = numbers[6:9]
    sub_unique = set(sub_list)
    if len(sub_unique) < 2:
        return None
    smallest = min(sub_unique)
    second_smallest = None
    for num in sub_unique:
        if num > smallest and (second_smallest is None or num < second_smallest):
            second_smallest = num
    return second_smallest