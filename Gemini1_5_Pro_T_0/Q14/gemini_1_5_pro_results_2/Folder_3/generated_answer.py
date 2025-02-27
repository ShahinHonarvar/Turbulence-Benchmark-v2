def find_second_smallest_num(numbers):
    if len(numbers) < 56 or len(numbers) < 28:
        return None
    else:
        new_list = sorted(numbers[27:56])
        if len(new_list) > 1:
            return new_list[1]
        else:
            return None