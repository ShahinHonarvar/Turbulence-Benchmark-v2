from itertools import islice, count

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in count(i + 1):
            index = j % len(circular_list)
            if product * circular_list[index] == 37:
                product *= circular_list[index]
                sublist.append(circular_list[index])
            else:
                break
        if len(sublist) > 1:
            result.append(sublist)
    return result