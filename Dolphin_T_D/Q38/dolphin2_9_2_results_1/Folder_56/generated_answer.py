def find_subset_of_length_n(nums):
    n = 60
    return len([combo for combo in itertools.combinations(nums, n)])