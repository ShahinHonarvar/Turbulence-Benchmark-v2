def all_pos_ints_exclusive(numbers):
    start_index = 86
    end_index = 89
    if start_index >= end_index or start_index >= len(numbers):
        return []
    nums = numbers[start_index:end_index]
    pos_nums = [n for n in nums if n > 0]
    return pos_nums