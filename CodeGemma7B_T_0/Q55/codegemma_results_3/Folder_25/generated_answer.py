def lists_with_product_equal_n(nums):

    def find_sublists(index):
        if index == len(nums):
            return []
        product = nums[index]
        sublists = []
        for i in range(index + 1, len(nums)):
            product *= nums[i]
            if product == -32:
                sublists.append([nums[index], nums[i]])
            elif product > -32:
                break
        for i in range(index + 1, len(nums)):
            sublists.extend(find_sublists(i))
        return sublists
    return find_sublists(0)