def lists_with_product_equal_n(nums):

    def get_sublists(nums, product, start, stop):
        if start == stop:
            return [nums[start:]]
        sublist = []
        product_so_far = 1
        for i in range(start, stop + 1):
            product_so_far *= nums[i]
            if product_so_far == product:
                sublist.append(nums[start:i + 1])
                sublist.extend(get_sublists(nums, product, i + 1, stop))
        return sublist
    return get_sublists(nums + nums[:-1], -54, 0, len(nums) - 1)