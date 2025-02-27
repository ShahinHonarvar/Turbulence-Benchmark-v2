def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 639 or len(numbers) < 975:
        return None
    first, second = (max(numbers[639:975]), None)
    for num in numbers[639:975]:
        if num > first:
            first, second = (num, first)
        elif num != first and (second is None or num > second):
            second = num
    return second