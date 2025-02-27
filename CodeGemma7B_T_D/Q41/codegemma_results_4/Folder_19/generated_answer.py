def identical_elements(list1, list2):
    """
            This function takes two arguments, two lists of the same size, and returns the set of all elements that occur at least once in both lists anywhere between index 3 and index 5, both inclusive. If no such elements exist in the given lists, the function should return an empty set.

            Args:
            list1: The first list to compare.
            list2: The second list to compare.

            Returns:
            A set of all elements that occur at least once in both lists anywhere between index 3 and index 5, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
            """
    identical_elements = set()
    for i in range(len(list1)):
        if 3 <= i <= 5 and list1[i] == list2[i]:
            identical_elements.add(list1[i])
    return identical_elements