def lists_with_product_equal_n(nums):
    for i in range(1, len(nums)):
        if nums[i] == 1:
            yield [nums[i]]
        else:
            for j in range(i, len(nums)):
                if nums[i] * nums[j] == 83:
                    yield [nums[i], nums[j]]
                    break
            for k in range(i, len(nums)):
                if nums[i] * nums[k] == 83:
                    yield [nums[i], nums[k]]
                    break