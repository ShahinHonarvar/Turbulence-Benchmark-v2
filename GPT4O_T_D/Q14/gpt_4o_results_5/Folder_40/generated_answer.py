def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    if len(first_three) < 2:
        return None
    first_three.sort()
    return first_three[1]