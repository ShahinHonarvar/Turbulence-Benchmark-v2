def lists_with_product_equal_n(circular_list: list[int]) -> list[list[int]]:

    def find_subarrays(arr, product):
        length = len(arr)
        result = []
        for size in range(1, length + 1):
            for start in range(0, length - size + 1):
                end = start + size - 1
                if arr[start] == 0 and product != 0:
                    continue
                if arr[start] < 0 and (product % 2 == 0 or size % 2 == 0):
                    continue
                if arr[start:end + 1] == [0] * size:
                    continue
                if product % arr[start] == 0:
                    temp = [arr[start]]
                    temp_prod = arr[start]
                    for idx in range(start + 1, end + 1):
                        temp_prod *= arr[idx]
                        if temp_prod == product:
                            result.append(temp + [arr[idx]])
                        temp.append(arr[idx])
                if product % arr[end] == 0:
                    temp = [arr[end]]
                    temp_prod = arr[end]
                    for idx in range(end - 1, start - 1, -1):
                        temp_prod *= arr[idx]
                        if temp_prod == product:
                            result.append([arr[idx]] + temp)
                        temp.insert(0, arr[idx])
        return result
    subarrays = find_subarrays(circular_list, -44)
    circular_subarrays = []
    for subarray in subarrays:
        for i in range(len(subarray)):
            circular_subarrays.append(subarray[i:] + subarray[:i])
    unique_subarrays = []
    for subarray in circular_subarrays:
        if subarray not in unique_subarrays:
            unique_subarrays.append(subarray)
    return unique_subarrays