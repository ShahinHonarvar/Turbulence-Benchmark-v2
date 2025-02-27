def lists_with_product_equal_n(circular_list):

    def find_sublists(arr, n):
        result = []
        length = len(arr)
        for start in range(length):
            product = 1
            sublist = []
            for end in range(start, start + length):
                product *= arr[end % length]
                sublist.append(arr[end % length])
                if product == n:
                    result.append(sublist.copy())
        return result
    return find_sublists(circular_list, -22)