def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    num_slice = numbers[31:73]
    num_set = set(num_slice)
    if len(num_set) < 2:
        return None
    return sorted(num_set)[1]