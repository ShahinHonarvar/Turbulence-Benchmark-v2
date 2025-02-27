def lists_with_product_equal_n(nums):
    """
            :type nums: circular list[int]
            :rtype: list[list[int]]
            """
    sets = []
    for i in range(len(nums)):
        start = i
        product = 1
        while True:
            if start >= len(nums):
                start = 0
            if product == -20:
                if nums[start] not in sets:
                    sets.append(nums[start])
            elif product != -20 and nums[start] == 0:
                break
            elif product != -20 and nums[start] != 0:
                product *= nums[start]
            start += 1
    if len(sets) == 0:
        return []
    else:
        return [[item] for item in sets]