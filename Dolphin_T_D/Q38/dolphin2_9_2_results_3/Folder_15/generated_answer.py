def find_subset_of_length_n(set_of_elements):

    def helper(set_of_elements, n):
        if n == 0:
            return 1
        elif len(set_of_elements) == 0:
            return 0
        else:
            return helper(set_of_elements - {set_of_elements.pop()}, n - 1) + helper(set_of_elements, n)
    return helper(set_of_elements, 10)