def lists_with_product_equal_n(circular_list):
    n = 6
    result = []
    size = len(circular_list)
    for i in range(size):
        for j in range(size):
            sublist = circular_list[i:j + 1]
            if len(sublist) > size:
                continue
            index = j + 1
            while index <= i + size:
                if index > size:
                    sublist.append(circular_list[index - size - 1])
                product = 1
                for x in sublist:
                    product *= x
                if product == n:
                    result.append(sublist.copy())
                index += 1
    return result