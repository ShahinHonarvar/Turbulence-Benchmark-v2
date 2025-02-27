def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def is_valid(index):
        return 0 <= index < n
    for start in range(n):
        product = 1
        temp_list = []
        index = start
        for _ in range(n):
            product *= circular_list[index]
            temp_list.append(circular_list[index])
            if product == 714:
                result.append(temp_list[:])
            index = (index + 1) % n
            if not is_valid(index):
                break
            if product == 0:
                break
    return result