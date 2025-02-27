def lists_with_product_equal_n(nums):

    def generate_sublists(nums):
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                res.append(nums[i:j + 1])
        return res
    sublists = generate_sublists(nums)
    res = [lst for lst in sublists if functools.reduce(lambda x, y: x * y, lst) == 36]
    return res or []