def lists_with_product_equal_n(circular_list):

    def find_subarrays(lst, target_product):
        length = len(lst)
        product = 1
        start = 0
        result = []
        for end in range(length):
            product *= lst[end]
            while product > target_product and start <= end:
                product //= lst[start]
                start += 1
            if product == target_product:
                result.append(lst[start:end + 1])
        return result
    result = []
    for i in range(len(circular_list)):
        subarrays = find_subarrays(circular_list[i:] + circular_list[:i], 57)
        result.extend(subarrays)
    return result