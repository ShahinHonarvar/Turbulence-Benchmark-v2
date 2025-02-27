def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 100 or len(numbers) < 62:
        return None
    first, second = (max(numbers[62:100]), None)
    for num in numbers[62:100]:
        if num > first:
            second, first = (first, num)
        elif num != first and (second is None or num > second):
            second = num
    return second