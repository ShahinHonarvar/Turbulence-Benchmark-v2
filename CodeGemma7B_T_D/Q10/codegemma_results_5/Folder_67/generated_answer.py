def all_odd_ints_exclusive(nums):
    start_index = 49
    end_index = 74
    result = []
    for i in range(start_index, end_index):
        if i % 2 != 0:
            result.append(i)
    return result