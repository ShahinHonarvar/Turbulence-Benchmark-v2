def lists_with_product_equal_n(circular_list):

    def find_subarrays(arr, target, size):
        result = []
        for i in range(len(arr)):
            for j in range(i, min(i + size, len(arr))):
                if product(arr[i:j + 1]) == target:
                    result.append(arr[i:j + 1])
        return result

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j] + circular_list[0:j - len(circular_list) + 1]
            if product(sublist) == 3:
                result.append(sublist)
    return result