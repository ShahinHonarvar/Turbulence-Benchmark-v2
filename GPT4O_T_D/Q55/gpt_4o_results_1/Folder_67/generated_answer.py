def lists_with_product_equal_n(circular_list):

    def find_sublist(start, end):
        result = []
        product = 1
        for i in range(start, end):
            product *= circular_list[i % len(circular_list)]
            if product == 33:
                result.append(circular_list[start:end])
            elif product > 33 or i - start + 1 == len(circular_list):
                break
        return result
    results = []
    for start in range(len(circular_list)):
        for end in range(start + 1, start + len(circular_list) + 1):
            results.extend(find_sublist(start, end))
    return results