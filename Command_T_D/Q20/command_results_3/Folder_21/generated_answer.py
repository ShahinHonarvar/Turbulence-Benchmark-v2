def find_n_th_smallest_num(nums):
    sorted_nums = sorted(set(nums))
    num_groups = [[] for i in range(len(sorted_nums) + 1)]
    for i in range(1, len(sorted_nums) + 1):
        num_groups[i] = sorted_nums[:i]
    return num_groups[299][12]