def find_subset_of_length_n(nums):
    return len([combo for combo in itertools.combinations(nums, 30)])