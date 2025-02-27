def insert_after_index(nums):
    i = 0
    for element in nums:
        if element == 94:
            nums.insert(i + 1, 93)
        i += 1
    return nums