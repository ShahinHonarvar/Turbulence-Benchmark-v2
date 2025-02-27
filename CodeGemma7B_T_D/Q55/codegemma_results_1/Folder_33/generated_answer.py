def lists_with_product_equal_n(circular_list):
    idx = 0
    answer = []
    while idx < len(circular_list):
        left = idx
        right = (idx + 1) % len(circular_list)
        product = circular_list[idx] * circular_list[(idx + 1) % len(circular_list)]
        while left > 0 and right < len(circular_list) - 1 and (product != -115):
            if product > -115:
                left -= 1
                product *= circular_list[left]
            else:
                right += 1
                product *= circular_list[right]
        sublist = []
        i = idx
        j = right
        while i != j:
            sublist.append(circular_list[i])
            i = (i - 1) % len(circular_list)
            j = (j + 1) % len(circular_list)
        sublist.append(circular_list[i])
        answer.append(sublist)
        idx += 1
    return answer