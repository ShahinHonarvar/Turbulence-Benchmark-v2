def lists_with_product_equal_n(nums):
    rect_list = nums + nums
    sublists = []
    for i in range(len(rect_list)):
        for j in range(i + 1, len(rect_list)):
            sublist = rect_list[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -5:
                sublists.append(list(sublist))
    result = []
    for sublist in sublists:
        if sublist in nums:
            result.append(sublist)
    return result