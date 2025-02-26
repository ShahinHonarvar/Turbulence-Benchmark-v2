def find_second_largest_num(numbers):
    if len(numbers) < 3:
        return None
    first_three = numbers[:3]
    first_three.sort(reverse=True)
    return first_three[1]