def lists_with_product_equal_n(circular_list):

    def find_sublists(start, end):
        result = []
        product = 1
        count = 0
        while count < len(circular_list):
            product *= circular_list[end]
            if product == -81:
                sublist = []
                index = start
                sub_count = 0
                while sub_count < (end - start + 1) % len(circular_list):
                    sublist.append(circular_list[index])
                    index = (index + 1) % len(circular_list)
                    sub_count += 1
                result.append(sublist)
            end = (end + 1) % len(circular_list)
            count += 1
        return result
    all_sublists = []
    for i in range(len(circular_list)):
        sublists = find_sublists(i, i)
        all_sublists.extend(sublists)
    return all_sublists