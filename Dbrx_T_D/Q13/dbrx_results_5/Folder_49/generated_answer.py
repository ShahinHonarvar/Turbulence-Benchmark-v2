def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) - 200 < 80:
        return None
    first, second = (max(numbers[80:200]), None)
    for num in numbers[80:200]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second