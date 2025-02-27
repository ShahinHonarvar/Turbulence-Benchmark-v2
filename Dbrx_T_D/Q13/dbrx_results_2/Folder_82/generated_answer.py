def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers[20:201]) < 2:
        return None
    first, second = (max(numbers[20:201]), None)
    for num in numbers[20:201]:
        if num >= first:
            continue
        if second is None or num > second:
            second = num
    return second