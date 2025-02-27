from itertools import count

def lists_with_product_equal_n(circular_list):
    i = 0
    results = []
    while i < len(circular_list):
        product = circular_list[i]
        nums = [circular_list[i]]
        for j in count(i + 1):
            if j >= len(circular_list):
                j = 0
            product *= circular_list[j]
            nums.append(circular_list[j])
            if len(nums) > len(circular_list):
                break
            if product == -72:
                results.append(nums[:])
        i += 1
    return results