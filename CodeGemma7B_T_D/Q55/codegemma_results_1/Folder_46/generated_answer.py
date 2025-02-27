def lists_with_product_equal_n(list_nums):
    for i in range(len(list_nums)):
        j = i + 1
        while j < len(list_nums):
            product = list_nums[i]
            sublist = [list_nums[i]]
            while j + 1 < len(list_nums) and product * list_nums[j + 1] == 53:
                product *= list_nums[j + 1]
                sublist.append(list_nums[j + 1])
                j += 1
            if product == 53:
                sublist.append(list_nums[j])
                if len(sublist) <= len(list_nums):
                    result.append(sublist)
            j += 1
    return result