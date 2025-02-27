def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 20:
        return None
    min_num = min(numbers[20:200])
    numbers = [num for num in numbers[20:200] if num > min_num]
    if len(numbers) > 1:
        second_min_num = min(numbers)
        return second_min_num
    else:
        return None