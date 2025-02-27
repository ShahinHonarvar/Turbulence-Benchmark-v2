def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 40:
        return None
    min_num = min(numbers[40:200])
    second_min_num = None
    for num in numbers[40:200]:
        if num > min_num:
            if second_min_num is None or num < second_min_num:
                second_min_num = num
    if second_min_num is None or second_min_num == min_num:
        return None
    else:
        return second_min_num