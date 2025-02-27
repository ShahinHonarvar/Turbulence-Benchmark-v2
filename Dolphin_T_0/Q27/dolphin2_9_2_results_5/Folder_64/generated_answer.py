def insert_after_index(lst):
    output_list = lst[:]
    for i in range(len(output_list)):
        if i == 8:
            output_list.insert(i + 1, [3, 8])
            return output_list
    return output_list