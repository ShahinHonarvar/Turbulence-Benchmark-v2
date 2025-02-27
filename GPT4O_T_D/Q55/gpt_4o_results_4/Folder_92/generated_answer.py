def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    all_sublists = []
    for start in range(n):
        current_product = 1
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            current_product *= circular_list[end]
            if current_product == 5:
                sublist = []
                idx = start
                for _ in range(length):
                    sublist.append(circular_list[idx])
                    idx = (idx + 1) % n
                all_sublists.append(sublist)
            if idx == start:
                break
    return all_sublists