def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp not in result and temp != []:
                result.append(temp)
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    subarrays = find_subarrays(circular_list, -115, len(circular_list))
    result = [arr for arr in subarrays if product(arr) == -115]
    return result