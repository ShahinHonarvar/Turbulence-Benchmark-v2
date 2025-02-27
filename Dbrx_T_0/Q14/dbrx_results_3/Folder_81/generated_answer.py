def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100 or len(numbers) < 10:
        return None
    min_num = min(numbers[10:100])
    second_min_num = None
    for num in numbers[10:100]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    if second_min_num is None or second_min_num == min_num:
        return None
    else:
        return second_min_num