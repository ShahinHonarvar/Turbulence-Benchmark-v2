def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp not in result and prod(temp) == target:
                result.append(temp)
        return result

    def prod(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    return find_subarrays(circular_list, -82, len(circular_list))