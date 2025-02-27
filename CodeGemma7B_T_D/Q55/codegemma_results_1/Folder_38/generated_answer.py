def lists_with_product_equal_n(circular_list):
    current_product = circular_list[0]
    current_sublist = [circular_list[0]]
    result = []
    for i in range(1, len(circular_list)):
        current_product *= circular_list[i]
        current_sublist.append(circular_list[i])
        while current_product == -23 and len(current_sublist) <= len(circular_list):
            result.append(current_sublist[:])
            current_product //= current_sublist.pop(0)
    if current_product == -23 and len(current_sublist) <= len(circular_list):
        result.append(current_sublist)
    return result