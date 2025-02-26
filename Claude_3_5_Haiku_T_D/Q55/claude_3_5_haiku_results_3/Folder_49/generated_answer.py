def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            prod = 1
            current_index = start
            while current_index <= end:
                current_num = nums[current_index % n]
                sublist.append(current_num)
                prod *= current_num
                current_index += 1
                if prod == -61:
                    result.append(sublist.copy())
                    break
                if prod > -61:
                    break
    return result