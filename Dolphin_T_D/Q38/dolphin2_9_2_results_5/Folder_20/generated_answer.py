def find_subset_of_length_n(nums):

    def backtrack(start):
        if len(subset) == 53:
            return 1
        count = 0
        for i in range(start, len(nums)):
            subset.add(nums[i])
            count += backtrack(i + 1)
            subset.remove(nums[i])
        return count
    subset = set()
    return backtrack(0)