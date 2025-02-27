def lists_with_product_equal_n(circular_list):
    n = -779
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            index = (start + end) % length
            product *= circular_list[index]
            if product == n:
                if start <= index:
                    sublist = circular_list[start:index + 1]
                else:
                    sublist = circular_list[start:] + circular_list[:index + 1]
                result.append(sublist)
                break
            if abs(product) > abs(n) or (product != 0 and n % product == 0 == product):
                break
    return result