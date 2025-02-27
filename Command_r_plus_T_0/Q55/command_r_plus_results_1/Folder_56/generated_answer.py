def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp not in result and product(temp) == target:
                result.append(temp)
        return result

    def product(lst):
        p = 1
        for num in lst:
            p *= num
        return p
    n = len(circular_list)
    target = -65
    result = find_subarrays(circular_list, target, n)
    return result