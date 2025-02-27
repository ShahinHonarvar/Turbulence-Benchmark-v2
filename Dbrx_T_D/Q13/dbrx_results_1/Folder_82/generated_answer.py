def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 200 - 20 + 1:
        return None
    first, second = (max(numbers[20:200]), float('-inf'))
    for num in numbers[20:200]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if second != float('-inf') else None