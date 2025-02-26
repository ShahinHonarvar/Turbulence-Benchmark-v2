def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    first_two = numbers[:2]
    if first_two[0] > first_two[1]:
        return first_two[1]
    else:
        return first_two[0]