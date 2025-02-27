def find_subset_of_length_n(a, n):

    def find_subset_of_length_n_aux(nums, current_subset, index, n):
        if len(current_subset) == n:
            return 1
        if index >= len(nums):
            return 0
        current_subset.append(nums[index])
        count = find_subset_of_length_n_aux(nums, current_subset, index + 1, n)
        current_subset.pop()
        count += find_subset_of_length_n_aux(nums, current_subset, index + 1, n)
        return count
    return find_subset_of_length_n_aux(a, [], 0, n)