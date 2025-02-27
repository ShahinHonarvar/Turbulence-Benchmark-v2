def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, target, n):
        result = []
        for i in range(n):
            temp = [arr[(i + j) % n] for j in range(n)]
            if temp.count(-1) == 0 and temp.count(2) == 0 and (temp.count(9) == 0):
                continue
            if temp.count(-1) % 2 == 0 and temp.count(2) % 2 == 0 and (temp.count(9) % 2 == 0):
                continue
            if temp.count(-1) % 2 == 0 and temp.count(2) % 2 == 1 and (temp.count(9) % 2 == 1):
                continue
            if temp.count(-1) % 2 == 1 and temp.count(2) % 2 == 0 and (temp.count(9) % 2 == 1):
                continue
            if temp.count(-1) % 2 == 1 and temp.count(2) % 2 == 1 and (temp.count(9) % 2 == 0):
                continue
            if temp.count(-1) % 2 == 0 and temp.count(2) % 2 == 1 and (temp.count(9) % 2 == 0):
                continue
            if temp.count(-1) % 2 == 1 and temp.count(2) % 2 == 0 and (temp.count(9) % 2 == 0):
                continue
            if temp.count(-1) % 2 == 0 and temp.count(2) % 2 == 0 and (temp.count(9) % 2 == 1):
                continue
            result.append(temp)
        return result
    subarrays = find_subarrays(circular_list, -18, len(circular_list))
    return [sublist for sublist in subarrays if prod(sublist) == -18]