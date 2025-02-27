def sums_with_product_equal_n(circular_list):
    """Returns a list of contiguous sublists such that their product is equal to n."""
    product = 48
    sublists = []
    current_size = 0
    current_product = 1
    for num in circular_list + circular_list + circular_list:
        current_product *= num
        current_size += 1
        while current_product >= product and current_size > 0:
            if current_product == product:
                sublists.append(circular_list[len(circular_list) - current_size:len(circular_list)])
            current_product //= circular_list[(len(circular_list) - current_size + len(circular_list)) % len(circular_list)]
            current_size -= 1
    return sublists