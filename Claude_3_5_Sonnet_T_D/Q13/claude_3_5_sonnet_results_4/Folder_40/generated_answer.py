def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    sorted_first_three = sorted(first_three, reverse=True)
    return sorted_first_three[1] if len(sorted_first_three) > 1 else None