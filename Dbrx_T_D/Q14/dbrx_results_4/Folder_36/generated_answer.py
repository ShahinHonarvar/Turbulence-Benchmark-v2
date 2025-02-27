def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not all((isinstance(num, (int, float)) for num in numbers)):
        return None
    first_two_smallest = []
    for num in numbers[209:557]:
        if not first_two_smallest or first_two_smallest[0] > num:
            first_two_smallest = [num]
        elif first_two_smallest and first_two_smallest[0] < num < first_two_smallest[1]:
            first_two_smallest.append(num)
    return first_two_smallest[1] if len(first_two_smallest) > 1 else None