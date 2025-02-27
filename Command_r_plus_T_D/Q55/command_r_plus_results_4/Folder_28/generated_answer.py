from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def product_equal_n(sublist: List[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 85
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equal_n(sublist):
                result.append(sublist)
    return result