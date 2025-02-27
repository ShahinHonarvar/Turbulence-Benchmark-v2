def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp not in result and temp.count(-1) % 2 == 0 and (prod(temp) == target):
                result.append(temp)
        return result

    def prod(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    sublists = find_subarrays(circular_list, -115, len(circular_list))
    return sublists