def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(n):
            sublist = []
            product = 1
            for i in range(start, start + n):
                index = i % n
                sublist.append(circular_list[index])
                product *= circular_list[index]
                if product == 91:
                    result.append(sublist[:])
                elif product > 91:
                    break
                if i - start + 1 == n:
                    break
            if start == end:
                break
    return result