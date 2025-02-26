def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    sorted_three = sorted(first_three)
    if len(sorted_three) >= 2:
        return sorted_three[1]
    else:
        return None