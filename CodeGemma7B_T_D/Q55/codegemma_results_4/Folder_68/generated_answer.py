from itertools import combinations

def lists_with_product_equal_n(circular_list):
    end = len(circular_list)
    result = []
    for j in range(0, end):
        for k in range(j + 1, end):
            circular_list_temp = circular_list[j:k + 1]
            temp = [circular_list_temp[0]]
            product = circular_list_temp[0]
            for i in range(1, len(circular_list_temp)):
                product *= circular_list_temp[i]
                temp.append(circular_list_temp[i])
            if product == 6 and temp not in result:
                result.append(temp)
    return result