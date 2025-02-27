def find_second_largest_num(numbers):
    if not 30 <= 200 < len(numbers):
        return None
    segment = numbers[200:30:-1]
    if len(segment) < 2:
        return None
    max_num = max(segment)
    second_max = None
    for num in segment:
        if num < max_num and (second_max is None or num > second_max):
            second_max = num
    return second_max