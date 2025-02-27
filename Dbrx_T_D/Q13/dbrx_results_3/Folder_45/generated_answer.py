def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 201:
        return None
    max_num = max(numbers[30:200])
    second_num = None
    for num in numbers[30:200]:
        if num < max_num and (second_num is None or num > second_num):
            second_num = num
    if second_num is None:
        return None
    else:
        return second_num