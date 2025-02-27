def find_subset_of_length_n(my_set):
    if len(my_set) == 27:
        return 1 + find_subset_of_length_n(my_set.copy())
    elif len(my_set) > 27:
        return len(my_set) * find_subset_of_length_n(my_set.copy()).remove(my_set.pop())
    else:
        return 0