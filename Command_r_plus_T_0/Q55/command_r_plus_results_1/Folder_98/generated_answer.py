def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                if product == 1:
                    result.append(arr[start:start + size])
                elif product == -1:
                    if arr[start] < 0 and all((x > 0 for x in arr[start + 1:start + size])):
                        result.append(arr[start:start + size])
                    elif arr[start] > 0 and all((x < 0 for x in arr[start + 1:start + size])):
                        result.append(arr[start:start + size])
        return result
    subarrays = find_subarrays(circular_list, -1)
    subarrays_with_product_n = [subarray for subarray in subarrays if -1 in [prod for prod in map(lambda x: prod == -1, [prod for prod in [reduce(lambda x, y: x * y, subarray[i:j]) for i in range(len(subarray))] for j in range(1, len(subarray) + 1)])]]
    return subarrays_with_product_n