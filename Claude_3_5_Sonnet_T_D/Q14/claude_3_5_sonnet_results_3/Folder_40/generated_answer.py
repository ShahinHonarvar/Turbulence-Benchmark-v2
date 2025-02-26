def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    sorted_first_three = sorted(first_three)
    if len(sorted_first_three) < 2:
        return None
    return sorted_first_three[1]