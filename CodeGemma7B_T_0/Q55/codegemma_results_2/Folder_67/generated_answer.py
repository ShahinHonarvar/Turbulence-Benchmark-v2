from itertools import combinations

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            sublist = [circular_list[i]]
            for k in range(j + 1, len(circular_list)):
                if product * circular_list[k] == 33:
                    sublist.append(circular_list[k])
                    break
            if product * circular_list[j] == 33:
                sublist.append(circular_list[j])
            if len(sublist) > 1 and sublist in result:
                continue
            if len(sublist) > 1:
                result.append(sublist)
    return result