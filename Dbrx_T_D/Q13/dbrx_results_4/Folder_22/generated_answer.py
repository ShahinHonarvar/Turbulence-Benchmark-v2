def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers[40:201]) < 2:
        return None
    first, second = (max(numbers[40:201]), None)
    for num in numbers[40:201]:
        if num > first:
            second = first
            first = num
        elif num > second and num < first:
            second = num
    return second