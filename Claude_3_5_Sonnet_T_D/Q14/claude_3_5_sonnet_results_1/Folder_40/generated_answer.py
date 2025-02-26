def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    sorted_first_three = sorted(first_three)
    return sorted_first_three[1] if len(sorted_first_three) >= 2 else None