def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 10:
        return None
    min_num = min((num for num in numbers[8:10]))
    second_num = None
    for num in numbers[8:10]:
        if num > min_num:
            second_num = min(second_num, num) if second_num is not None else num
    return second_num