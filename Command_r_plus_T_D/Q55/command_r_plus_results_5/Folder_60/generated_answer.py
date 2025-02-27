from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def get_product(sublist: List[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def generate_sublists(circular_list: List[int], product: int) -> List[List[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + 1):
                sublist = circular_list[i:j]
                if get_product(sublist) == product:
                    sublists.append(sublist)
        return sublists
    return generate_sublists(circular_list, 49)