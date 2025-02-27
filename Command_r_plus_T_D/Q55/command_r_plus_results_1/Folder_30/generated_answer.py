from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(lst, product):
        length = len(lst)
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    if lst[i] == product:
                        yield [lst[i]]
                else:
                    subarray = lst[i:j + 1]
                    if prod(subarray) == product:
                        yield subarray

    def prod(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    result = []
    for sublist in find_subarrays(circular_list, 99):
        result.append(sublist)
    return result