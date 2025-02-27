def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 775 or len(numbers) < 668:
        return None
    first, second = (max(numbers[667:775], default=None), None)
    for num in numbers[667:775]:
        if num < first:
            second = num
            break
    for num in numbers[667:775]:
        if first > num > second:
            second = num
    return second