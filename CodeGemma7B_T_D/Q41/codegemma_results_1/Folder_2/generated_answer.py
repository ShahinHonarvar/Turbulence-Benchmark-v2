def identical_elements(first_list, second_list):
    """Since the problem requires to obtain the elements that occur at least once in both lists anywhere between index 15 and index 39, both inclusive, I will slice the lists on the arguments starting from index 15 up to and including index 39 on both lists."""
    first_list_slice = first_list[15:40]
    second_list_slice = second_list[15:40]
    result_set = set(first_list_slice) & set(second_list_slice)
    if not result_set:
        return set()
    else:
        return result_set