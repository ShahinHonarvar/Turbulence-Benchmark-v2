def find_second_smallest_num(numbers):
    if len(numbers[17:79]) < 2:
        return None
    smallest_two = []
    for num in numbers[17:79]:
        if not smallest_two or num < smallest_two[0]:
            smallest_two = [num]
        elif num > smallest_two[0] and (not smallest_two[1] or num < smallest_two[1]):
            smallest_two.append(num)
        if len(smallest_two) == 3:
            smallest_two.pop(0)
    return None if len(smallest_two) < 2 else smallest_two[1]