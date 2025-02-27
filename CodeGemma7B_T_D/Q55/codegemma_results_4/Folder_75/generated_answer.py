def lists_with_product_equal_n(nums):
    for start in range(len(nums)):
        product = nums[start]
        end = start
        while end + 1 < len(nums):
            end += 1
            product *= nums[end]
            if product == 13:
                return [[*nums[start:end + 1]]]
            elif product > 13:
                break
    return []