def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 20:
        return None
    max_num = max(numbers[20:200])
    numbers = [num for num in numbers[20:200] if num != max_num]
    if len(numbers) > 1:
        second_max_num = max(numbers)
        if second_max_num != max_num:
            return second_max_num
    return None