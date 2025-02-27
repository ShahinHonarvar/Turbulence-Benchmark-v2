def lists_with_product_equal_n(data):
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            if prod(data[i:j + 1]) == -17:
                result.append(data[i:j + 1])
    return result

def prod(nums):
    p = 1
    for n in nums:
        p *= n
    return p