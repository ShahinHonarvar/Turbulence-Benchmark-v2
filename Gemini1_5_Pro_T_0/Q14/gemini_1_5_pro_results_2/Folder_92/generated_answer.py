def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    elif numbers[0] < numbers[1]:
        return numbers[1]
    else:
        return numbers[0]