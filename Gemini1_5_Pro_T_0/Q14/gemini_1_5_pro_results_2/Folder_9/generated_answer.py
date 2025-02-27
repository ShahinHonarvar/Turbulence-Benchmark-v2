def find_second_smallest_num(numbers):
    if len(numbers) < 201 or len(numbers[:70]) == len(numbers[:201]):
        return None
    else:
        new_list = sorted(numbers[70:201])
        return new_list[1]