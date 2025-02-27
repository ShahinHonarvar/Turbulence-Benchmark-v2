def all_even_ints_exclusive(nums):
    result = []
    for i in range(389, 748):
        if nums[i] % 2 == 0 and i != 748:
            result.append(nums[i])
            if i == len(nums) - 1 and (not result):
                return []
    return result