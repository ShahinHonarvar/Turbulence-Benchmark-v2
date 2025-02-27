from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def product_equal_45(sublist: List[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 45
    all_sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i:j]
            if product_equal_45(sublist):
                all_sublists.append(sublist)
    return all_sublists