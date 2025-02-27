def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_two = [numbers[0], numbers[1]]
    min_two.sort()
    for num in numbers[2:]:
        if num < min_two[1]:
            if num > min_two[0]:
                min_two[1] = num
            elif num < min_two[0]:
                min_two[0], min_two[1] = (num, min_two[0])
    if min_two[0] == min_two[1]:
        return None
    else:
        return min_two[1]