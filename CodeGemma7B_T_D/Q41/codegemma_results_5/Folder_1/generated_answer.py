def identical_elements(list_one, list_two):
    """
            Identifies elements that occur in both lists between indices 31 and 72, inclusive.

            Args:
                list_one: The first list.
                list_two: The second list.

            Returns:
                A set of elements that occur at least once in both lists between indices 31 and 72, inclusive. An empty set is returned if no such elements exist.
            """
    set_one = set(list_one)
    set_two = set(list_two)
    identical_set = set_one.intersection(set_two)
    filtered_identical_set = {element for element in identical_set if list_one.index(element) >= 31 and list_two.index(element) >= 31 and (list_one.index(element) <= 72) and (list_two.index(element) <= 72)}
    return filtered_identical_set or set()