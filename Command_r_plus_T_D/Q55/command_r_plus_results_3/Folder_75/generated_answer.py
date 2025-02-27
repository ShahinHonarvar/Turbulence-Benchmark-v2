from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def product_equal_n(sublist: List[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 13
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j] % n
            if product_equal_n(sublist):
                result.append(sublist)
    return result