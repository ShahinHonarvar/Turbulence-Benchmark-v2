def lists_with_product_equal_n(circular_list):
    nums = CircularList(circular_list)
    results = []
    size = len(circular_list)
    for i in range(size):
        for j in range(i + 1, size):
            product = nums[i]
            temp = [nums[i]]
            k = j + 1
            while k < size and product * nums[k] <= 93:
                temp.append(nums[k])
                product *= nums[k]
                k += 1
            if product == 93 and len(temp) <= size:
                results.append(temp)
    return results