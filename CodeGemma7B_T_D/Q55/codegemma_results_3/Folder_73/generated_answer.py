def lists_with_product_equal_n(circular_list):

    def is_circular_list_valid(circular_list):
        """Checks if a given list is a circular list."""
        if not circular_list:
            return False
        current_element = circular_list[0]
        for i in range(1, len(circular_list)):
            if circular_list[i] == current_element:
                return True
            current_element = circular_list[i]
        return False
    if not is_circular_list_valid(circular_list):
        raise ValueError('The given list is not a circular list. It is empty or the beginning and the end of the list do not match.')
    unique_sublists = []
    for i in range(len(circular_list)):
        current_element = circular_list[i]
        current_sublist = [current_element]
        for j in range(i + 1, len(circular_list)):
            next_element = circular_list[(j + 1) % len(circular_list)]
            if next_element == current_element:
                unique_sublists.append(current_sublist)
            if current_element * next_element == 40:
                current_sublist.append(next_element)
            current_element = next_element
        if len(current_sublist) > 0:
            unique_sublists.append(current_sublist)
    return unique_sublists