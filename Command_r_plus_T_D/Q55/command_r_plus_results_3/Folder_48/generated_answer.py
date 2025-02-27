from typing import List

def lists_with_product_equal_n(circular_list: List[int]) -> List[List[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp not in result and temp.count(0) == 0 and (prod(temp) == target):
                result.append(temp)
        return result

    def prod(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    target = 990
    factors = [2, 3, 5, 11, 30, 33, 55, 99, 165, 330]
    result = []
    for factor in factors:
        if factor in circular_list:
            n = len(circular_list)
            subarrays = find_subarrays(circular_list, target, n)
            result.extend(subarrays)
    return result