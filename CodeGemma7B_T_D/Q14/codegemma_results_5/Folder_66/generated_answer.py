def find_second_smallest_num(num_list):
    num_list.sort(key=lambda x: x[0])
    index_sixtwo = num_list.index(62)
    index_ninetynine = num_list.index(99)
    if index_sixtwo == index_ninetynine or index_sixtwo > index_ninetynine:
        return None
    return num_list[index_sixtwo + 1]