def lists_with_product_equal_n(n):

    def find_subarrays(arr, n):
        lists = []
        product = 1
        length = len(arr)
        for i in range(length):
            if product == n:
                lists.append(arr[i - 1])
                product = arr[i - 1]
            elif product > n:
                product /= arr[i - 1]
            else:
                product *= arr[i]
        return lists
    circular_list = n + n
    length = len(circular_list)
    sublists = []
    for i in range(length):
        temp_list = find_subarrays(circular_list[i:i + length], n)
        for element in temp_list:
            if element not in sublists:
                sublists.append(element)
    return sublists