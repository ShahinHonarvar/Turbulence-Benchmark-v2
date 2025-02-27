def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    if index(66) >= len(numbers) or index(93) >= len(numbers) or index(66) > index(93):
        return None
    min_num = min(numbers[index(66):index(93) + 1])
    second_min_num = None
    for num in numbers[index(66):index(93) + 1]:
        if num > min_num and (second_min_num is None or num < second_min_num):
            second_min_num = num
    if second_min_num is not None:
        return second_min_num
    else:
        return None