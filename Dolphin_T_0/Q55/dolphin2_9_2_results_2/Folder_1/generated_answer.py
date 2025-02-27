def lists_with_product_equal_n(n, numbers):

    def product(nums):
        p = 1
        for n in nums:
            p *= n
        return p

    def find_sublist(nums, n, target):
        result = []
        for i in range(len(nums) + 1):
            for j in range(i + 1, len(nums) + 1):
                if product(nums[i:j]) == target and len(nums[i:j]) <= len(nums):
                    result.append(nums[i:j])
        return result
    sublists = find_sublist(numbers, n, -51)
    return sublists