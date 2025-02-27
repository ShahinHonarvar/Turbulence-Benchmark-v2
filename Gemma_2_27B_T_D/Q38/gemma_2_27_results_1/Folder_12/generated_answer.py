def find_subset_of_length_n(input_set):
    count = 0
    for element in input_set:
        for other_element in input_set:
            if element != other_element:
                subset = {element, other_element}
                if len(subset) == 27:
                    count += 1
    return count