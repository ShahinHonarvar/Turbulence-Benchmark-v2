def lists_with_product_equal_n(circular_list):
    n = -30
    sub_lists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sub_list = circular_list[i:j + 1]
            if len(sub_list) < len(circular_list):
                product = 1
                for x in sub_list:
                    product *= x
                if product == n:
                    sub_lists.append(sub_list)
            if j == len(circular_list) + i - 1:
                sub_list = circular_list[i:] + circular_list[:j - len(circular_list) + 1]
                product = 1
                for x in sub_list:
                    product *= x
                if product == n:
                    sub_lists.append(sub_list)
    return sub_lists