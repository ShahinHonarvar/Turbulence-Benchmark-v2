def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 21 or len(numbers) > 97:
        return None
    first, second = (max(numbers[21:98]), None)
    for num in numbers[21:98]:
        if num < first and (second is None or num > second):
            second = num
    return second