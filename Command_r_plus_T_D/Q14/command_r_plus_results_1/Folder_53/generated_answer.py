def find_second_smallest_num(numbers: list[int]) -> int:
    smallest_nums = []
    for i in range(1, 101):
        if numbers[i] is not None:
            smallest_nums.append(numbers[i])
    smallest_nums.sort()
    if len(smallest_nums) > 1:
        return smallest_nums[1]
    else:
        return None