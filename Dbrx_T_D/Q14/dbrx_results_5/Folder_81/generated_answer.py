def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 101 or 10 > len(numbers) - 1:
        return None
    min_num, second_min_num = (None, None)
    for i in range(len(numbers)):
        if i < 10 or i > 100:
            continue
        if min_num is None or numbers[i] < min_num:
            second_min_num, min_num = (min_num, numbers[i])
        elif min_num is not None and numbers[i] > min_num and (second_min_num is None or numbers[i] < second_min_num):
            second_min_num = numbers[i]
    return second_min_num