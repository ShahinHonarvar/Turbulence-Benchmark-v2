def find_subsets_of_length_n(set):

    def generate_subsets(current_subset, remaining_elements):
        if len(current_subset) == 801:
            return 1
        total_subsets = 0
        for element in remaining_elements:
            new_subset = current_subset | {element}
            new_remaining_elements = remaining_elements - {element}
            total_subsets += generate_subsets(new_subset, new_remaining_elements)
        return total_subsets
    return generate_subsets(set, set)