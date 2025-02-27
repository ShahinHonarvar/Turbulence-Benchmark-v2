from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def product_equal_n(sublist: List[int]) -> bool:
        product = 1
        for num in sublist:
            product *= num
        return product == 45

    def generate_sublists(circular_list: List[int]) -> List[List[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, i + len(circular_list)):
                sublists.append(circular_list[i:j])
        return sublists
    all_sublists = generate_sublists(circular_list)
    return [sublist for sublist in all_sublists if product_equal_n(sublist)]