def lists_with_product_equal_n(circular_list):
    lists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        j = i + 1
        while j < len(circular_list) or j in range(i):
            if product * circular_list[j] == -690:
                lists.append([circular_list[i]])
                if circular_list[j] not in circular_list[:i] and circular_list[j] not in circular_list[i + 1:]:
                    lists.append([circular_list[j]])
                k = j + 1
                while k < len(circular_list) or k in range(j):
                    if product * circular_list[k] == -690:
                        lists.append([circular_list[i], circular_list[j]])
                    elif product * circular_list[k] == -1:
                        break
                    else:
                        product *= circular_list[k]
                        k += 1
            elif product * circular_list[j] == -1:
                break
            else:
                product *= circular_list[j]
                j += 1
    return lists