from itertools import islice

def lists_with_product_equal_n(my_list):

    def sublists(my_list, start=0, end=1):
        if end > len(my_list):
            return []
        current_sublist = my_list[start:end]
        sublists_of_current = []
        if product(current_sublist) == 93:
            sublists_of_current.append(current_sublist.copy())
        if end < len(my_list):
            sublists_of_current += sublists(my_list, start + 1, end + 1)
        if start < len(my_list) - 1:
            sublists_of_current += sublists(my_list, start, end + 1)
        return sublists_of_current

    def product(my_list):
        result = 1
        for num in my_list:
            result *= num
        return result
    result = []
    for i in range(len(my_list)):
        result.extend(sublists(my_list[i:] + my_list[:i]))
    return result