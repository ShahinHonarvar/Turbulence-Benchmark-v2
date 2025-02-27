def lists_with_product_equal_n(circular_list):
    negative_sign_count = 0
    product_so_far = 1
    filter_index = 0
    results = []
    for i, num in enumerate(circular_list):
        if num < 0:
            negative_sign_count += 1
        product_so_far *= num
        while negative_sign_count > 1 and product_so_far < 0 or (negative_sign_count % 2 == 1 and product_so_far > 0):
            product_so_far //= circular_list[filter_index]
            filter_index += 1
            if circular_list[filter_index] < 0:
                negative_sign_count -= 1
        if product_so_far == -51:
            results.append(circular_list[filter_index:i + 1])
    return results