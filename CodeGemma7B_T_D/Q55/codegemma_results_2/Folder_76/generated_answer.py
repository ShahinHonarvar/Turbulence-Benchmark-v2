from itertools import cycle

def lists_with_product_equal_n(nums):
    target_product = 247

    def generate_sublists(start_index, nums):
        product = 1
        sublist = []
        for i in range(start_index, len(nums)):
            product *= nums[i]
            sublist.append(nums[i])
            if product == target_product:
                yield sublist
            if product > target_product:
                break
        for i in range(0, start_index):
            product *= nums[i]
            sublist.append(nums[i])
            if product == target_product:
                yield sublist
            if product > target_product:
                break
    for i in range(len(nums)):
        for sublist in generate_sublists(i, nums):
            yield sublist