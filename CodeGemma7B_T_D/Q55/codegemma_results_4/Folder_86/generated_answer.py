from itertools import islice

def lists_with_product_equal_n(nums):
    products = {}
    result = []
    for i in range(len(nums)):
        product = nums[i]
        for j in islice(nums, i + 1, None):
            product *= j
            if product == -779:
                result.append(nums[i:j + 1])
            elif product in products:
                result.extend(products[product])
            else:
                products[product] = [nums[i:j + 1]]
    return result