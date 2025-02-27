def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 270:
        return None
    min_num = float('infinity')
    second_min_num = float('infinity')
    for num in numbers[70:201]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('infinity'):
        return None
    else:
        return second_min_num