def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) - 70 < 2:
        return None
    min_num = min(numbers[70:200])
    second_num = float('inf')
    found_min = False
    for num in numbers[70:200]:
        if num == min_num:
            found_min = True
        elif num < second_num:
            second_num = num
    return second_num if found_min else None