def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 61 - 16 + 1:
        return None
    first, second = (max(numbers[16:61]), None)
    for num in numbers[16:61]:
        if num > first:
            second, first = (first, num)
        elif num > second and num < first:
            second = num
    return second