from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def get_product(sublist: List[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def find_sublists_with_product(product_target: int) -> List[List[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i, len(circular_list) + i):
                sublist = circular_list[i:j]
                if get_product(sublist) == product_target:
                    sublists.append(sublist)
        return sublists
    return find_sublists_with_product(43)