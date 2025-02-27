def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 200 < 200:
        return None
    first, second = (max(numbers[200]), None)
    for num in numbers[200:200 + 201]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    if second is not None:
        return second
    return None