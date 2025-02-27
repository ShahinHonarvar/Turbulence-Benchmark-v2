def lists_with_product_equal_n(circular_list):
    ans = []
    size = len(circular_list)
    for start in range(size):
        product = circular_list[start]
        sublist = [circular_list[start]]
        for i in range(start + 1, size):
            product *= circular_list[i]
            sublist.append(circular_list[i])
            if product == 632:
                ans.append(sublist[:])
            elif product > 632:
                break
        if start == len(circular_list) - 1:
            product = circular_list[0]
            sublist = [circular_list[0]]
            for i in range(1, start):
                product *= circular_list[i]
                sublist.append(circular_list[i])
                if product == 632:
                    ans.append(sublist[:])
                elif product > 632:
                    break
    return ans