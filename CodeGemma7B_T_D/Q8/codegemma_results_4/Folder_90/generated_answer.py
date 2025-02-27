def all_even_ints_exclusive(nums):
    """(list[int]) -> list[int]"""
    res = []
    for i in range(389, 748):
        if nums[i] % 2 == 0:
            res.append(nums[i])
    return res