from itertools import product

def lists_with_product_equal_n(nums):
    product_of_nums = 1
    for num in nums:
        product_of_nums *= num

    def find_sublists(product_of_nums_div_n):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sublist = nums[i:j]
                if product(sublist) == product_of_nums_div_n:
                    yield sublist
    return list(find_sublists(product_of_nums // -61))