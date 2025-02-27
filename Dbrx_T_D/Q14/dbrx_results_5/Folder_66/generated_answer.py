def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) <= (99 - 62) * 2:
        return None
    min_two = [None, None]
    for num in numbers[62:100]:
        if min_two[0] is None or num < min_two[0]:
            min_two = [num, min_two[0]]
        elif min_two[0] is not None and num > min_two[0] and (min_two[1] is None or num < min_two[1]):
            min_two[1] = num
    return min_two[1]