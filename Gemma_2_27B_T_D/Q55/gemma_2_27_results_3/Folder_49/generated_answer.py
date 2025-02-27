def lists_with_product_equal_n(nums):
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if i == 0 and j == len(nums):
                circular_list = nums
            else:
                circular_list = nums[i:j]
            product = 1
            for num in circular_list:
                product *= num
            if product == -61:
                sublists.append(circular_list)
    return sublists