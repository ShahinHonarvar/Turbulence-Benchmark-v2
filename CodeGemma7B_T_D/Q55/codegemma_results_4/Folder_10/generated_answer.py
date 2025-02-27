def lists_with_product_equal_n(nums):
    remainders = {0: [0]}
    product = 1
    result = []
    for i, num in enumerate(nums + nums):
        product *= num
        if product > 93 or product < -93:
            product = 1
            remainders = {0: [i + 1]}
        if product in remainders:
            for j in remainders[product]:
                if i - j >= len(nums):
                    result.append(nums[j:i + 1])
                elif i - j > 0:
                    result.append(nums[j:i])
        else:
            remainders[product] = [i]
    return list(set(map(tuple, result)))