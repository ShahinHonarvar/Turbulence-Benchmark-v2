def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    min_num = min(numbers[1:100])
    second_min_num = None
    for num in numbers[1:100]:
        if num > min_num:
            if second_min_num is None or num < second_min_num:
                second_min_num = num
                min_num = min(min_num, second_min_num)
    return second_min_num