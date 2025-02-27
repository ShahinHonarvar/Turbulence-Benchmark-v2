def all_neg_ints_exclusive(nums):
    extracted_nums = []
    for num in nums:
        if num < 0 and 38 < nums.index(num) < 52:
            extracted_nums.append(num)
    return extracted_nums