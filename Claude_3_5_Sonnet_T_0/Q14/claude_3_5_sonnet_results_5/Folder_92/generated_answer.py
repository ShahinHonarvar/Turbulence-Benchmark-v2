def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    first_two = numbers[:2]
    first_two.sort()
    return first_two[1]