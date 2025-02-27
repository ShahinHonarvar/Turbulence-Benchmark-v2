def find_subset_of_length_n(nums):

    def backtrack(subset, start):
        if len(subset) == 96:
            answer[0] += 1
            return
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
    answer = [0]
    backtrack([], 0)
    return answer[0]