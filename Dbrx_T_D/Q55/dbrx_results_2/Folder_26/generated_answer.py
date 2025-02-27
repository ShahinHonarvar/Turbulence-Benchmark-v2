from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_sublists_with_product(sublist: List[int], n: int) -> List[List[int]]:
        if not sublist:
            return []
        elif len(sublist) == 1 and sublist[0] == n:
            return [sublist]
        elif len(sublist) == 1 and sublist[0] != n:
            return []
        sublists = []
        for i in range(1, len(sublist) + 1):
            product = 1
            for j in range(i):
                product *= sublist[j]
                if product == n:
                    sublists.append(sublist[:j + 1])
                elif product > n or (j + 1 < len(sublist) and product > n / sublist[j + 1]):
                    break
        return sublists
    result = []
    for i in range(len(circular_list)):
        sublist = circular_list[i:] + circular_list[:i]
        result.extend(find_sublists_with_product(sublist, 93))
    return result