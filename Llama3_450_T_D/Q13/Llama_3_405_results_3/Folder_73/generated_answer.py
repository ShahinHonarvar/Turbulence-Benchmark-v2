def find_second_largest_num(num_list):
    if len(num_list) < 93:
        return None
    numbers = num_list[19:93]
    if len(numbers) < 2:
        return None
    numbers.sort(reverse=True)
    return numbers[1]