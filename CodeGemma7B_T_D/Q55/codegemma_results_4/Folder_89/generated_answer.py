def lists_with_product_equal_n(circular_list):
    copy = circular_list
    nums = set()
    for i in range(len(circular_list)):
        prod = 1
        indices = []
        index = i
        while prod * circular_list[index] <= 57:
            prod *= circular_list[index]
            indices.append(index)
            index = (index + 1) % len(circular_list)
            if prod == 57:
                nums.add(tuple((circular_list[i:j + 1] for i, j in zip(indices, indices[1:] + [len(circular_list) - 1]))))
    return list(nums)