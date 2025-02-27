def find_subset_of_length_n(set_of_elements):

    def combinations(current_combination, remaining_elements):
        if len(current_combination) == 35:
            return 1
        count = 0
        for element in remaining_elements:
            if element not in current_combination:
                count += combinations(current_combination + [element], remaining_elements - {element})
        return count
    return combinations([], set_of_elements)