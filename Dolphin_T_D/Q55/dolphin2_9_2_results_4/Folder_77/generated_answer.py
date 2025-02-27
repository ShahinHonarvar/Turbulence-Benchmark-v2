def find_sublist_with_product_equal_n(nums, n):
    sublists = []
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length + 1):
            if i == j:
                continue
            elif j == i + 1:
                product = nums[i]
            else:
                product = nums[i] * nums[j - 1]
            if product == n:
                sublists.append(nums[i:j])
    return sublists