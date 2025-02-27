def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    min_two = [None, None]
    for i in range(66, 78):
        if numbers[i] not in min_two:
            if min_two[0] is None or numbers[i] < min_two[0]:
                min_two[1] = min_two[0]
                min_two[0] = numbers[i]
            elif min_two[0] is not None and min_two[1] is None or numbers[i] < min_two[1]:
                min_two[1] = numbers[i]
    return min_two[1]