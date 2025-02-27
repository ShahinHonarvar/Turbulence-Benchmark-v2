def lists_with_product_equal_n(circular_list):

    def sublists_product(arr, n):
        length = len(arr)
        sublists = []
        for start in range(length):
            product = 1
            sublist = []
            for i in range(length):
                index = (start + i) % length
                if len(sublist) < length:
                    sublist.append(arr[index])
                    product *= arr[index]
                    if product == n:
                        sublists.append(sublist.copy())
        return sublists
    return sublists_product(circular_list, -7)