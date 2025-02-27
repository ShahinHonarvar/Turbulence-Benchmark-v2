def lists_with_product_equal_n(lst, product=91):

    def get_sublist(nums_sublist):
        return [num for num in nums_sublist if num % 2 == 0]
    circular_lst = lst + lst
    size = len(lst)
    locations = {}
    sublists = []
    for i, num in enumerate(circular_lst):
        for j in range(i + 1, size * 2):
            if num * circular_lst[j] % product == 0 and lst[j % size] not in locations:
                sublists.append(get_sublist(circular_lst[i:j]))
                locations[circular_lst[j % size]] = j
    final_sublists = sublists
    sublists = []
    for sublist in final_sublists:
        for i in range(size - len(sublist) + 1):
            temp = lst[i:i + len(sublist)]
            cyclic_temp = temp + temp
            if all((cyclic_temp[i] in sublist for i in range(len(temp)))):
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists