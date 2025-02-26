def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                actual_index = current_index % n
                sublist.append(lst[actual_index])
                product *= lst[actual_index]
                current_index += 1
                if product == -87:
                    result.append(sublist.copy())
                    break
    return result