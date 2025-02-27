def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= 87 - 25 + 1:
        return None
    first, second = (max(numbers[25:88]), None)
    for num in numbers[25:88]:
        if num < first:
            second, first = (first, num)
            break
    if second is not None:
        for num in numbers[25:88]:
            if num < first and num > second:
                second = num
    return second