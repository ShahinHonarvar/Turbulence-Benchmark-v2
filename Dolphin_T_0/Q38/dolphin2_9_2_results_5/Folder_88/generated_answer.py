def find_subset_of_length_n(nums):
    nums = list(nums)
    n = len(nums)
    subset_count = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if j - i == 46:
                subset_count += 1
    return subset_count