def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % n
                sublist.append(nums[actual_index])
                product *= nums[actual_index]
                if product == 54:
                    result.append(sublist.copy())
                    break
                current_index += 1
    return result