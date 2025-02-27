def lists_with_product_equal_n(circular_list):
    pairs = []
    for i in range(len(circular_list)):
        l, r = (i, i + 1)
        product = circular_list[i]
        while l >= 0 and r <= len(circular_list) - 1 and (product != 0):
            if product == 0 and (circular_list[l] == 0 or circular_list[r] == 0):
                pairs.append(circular_list[l:r + 1])
            product *= circular_list[r]
            r += 1
            if r == len(circular_list):
                r = 0
            product /= circular_list[l]
            l -= 1
            if l < 0:
                l = len(circular_list) - 1
    return pairs