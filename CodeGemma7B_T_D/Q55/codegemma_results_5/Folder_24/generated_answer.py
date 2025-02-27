def lists_with_product_equal_n(circular_list):
    lists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == -89:
                lists.append(sublist[:])
                break
            elif product > -89:
                break
            elif product < -89:
                if sublist[-1] > 0 or sublist[0] < 0:
                    product = product / sublist.pop(0)
                    sublist.append(circular_list[j])
                else:
                    product = product / sublist.pop()
                    sublist.append(circular_list[j])
    return lists