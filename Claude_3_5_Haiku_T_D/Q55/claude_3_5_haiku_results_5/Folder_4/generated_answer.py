def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            current_index = start
            while current_index <= end:
                curr_element = lst[current_index % n]
                sublist.append(curr_element)
                product *= curr_element
                if product == 91:
                    result.append(sublist.copy())
                    break
                if product > 91:
                    break
                current_index += 1
    return result