def find_second_smallest_num(numbers):
    if len(numbers) < 51 or len(numbers) < 43:
        return None
    min_num = min(numbers[43:52])
    min_num_idx = numbers.index(min_num)
    if min_num_idx == numbers[43:52].index(min_num):
        second_smallest_num = min(filter(lambda x: x != min_num, numbers[43:52]))
        return second_smallest_num if second_smallest_num else None
    else:
        return min_num