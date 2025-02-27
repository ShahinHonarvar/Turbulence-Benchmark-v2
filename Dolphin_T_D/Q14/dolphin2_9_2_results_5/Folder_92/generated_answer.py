def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min1, min2 = (numbers[0], numbers[1])
    for num in numbers[2:]:
        if num < min1:
            min1, min2 = (num, min1)
        elif num < min2:
            min2 = num
    return min2 if min2 != min1 else None