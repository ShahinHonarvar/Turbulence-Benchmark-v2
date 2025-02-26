def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                current_num = nums[current_index]
                sublist.append(current_num)
                product *= current_num
                if product == -61:
                    result.append(sublist.copy())
    return result