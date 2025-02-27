def all_neg_ints_inclusive(nums):
    output = []
    for num in nums:
        if num < 0:
            output.append(num)
    return output