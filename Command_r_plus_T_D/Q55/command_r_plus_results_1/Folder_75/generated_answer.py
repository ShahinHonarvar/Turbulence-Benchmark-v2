from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def get_product(sublist: List[int]) -> int:
        product = 1
        for num in sublist:
            product *= num
        return product

    def generate_sublists(circular_list: List[int]) -> List[List[int]]:
        sublists = []
        for i in range(len(circular_list)):
            for j in range(i + 1, len(circular_list) + i + 1):
                sublists.append(circular_list[i:j % len(circular_list)])
        return sublists
    sublists = generate_sublists(circular_list)
    return [sublist for sublist in sublists if get_product(sublist) == 13]