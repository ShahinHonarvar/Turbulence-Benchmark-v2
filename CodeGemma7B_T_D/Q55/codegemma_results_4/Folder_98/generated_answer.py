def lists_with_product_equal_n(circular_list):
    i = 0
    max_length = len(circular_list)
    products = [1] * len(circular_list)
    while i < len(circular_list):
        j = i - 1
        while j >= 0:
            products[j] *= circular_list[i]
            j -= 1
        i += 1
    sublists = []
    for i in range(len(circular_list)):
        if products[i] == -1:
            left = i
            right = i
            popped = 0
            while True:
                right = (right + 1) % len(circular_list)
                if products[right] == -1:
                    popped += 1
                    if popped == 2:
                        break
                if products[left] < 0:
                    break
                sublist = []
                prod = 1
                for k in range(left, right + 1):
                    prod *= circular_list[k]
                    sublist.append(circular_list[k])
                if prod == -1:
                    sublists.append(sublist)
                    products[left] = -1
                    left = (left - 1 + len(circular_list)) % len(circular_list)
                    right = (right - 1 + len(circular_list)) % len(circular_list)
    return sublists