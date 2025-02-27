def find_second_largest_num(num_list):
    """
            This function takes a list of numbers as input and returns the second largest number from
            index 56 to index 82, both inclusive. If there is no element at those indices,
            the function returns 'None'.
            """
    num_list.sort(reverse=True)
    if len(num_list) > 82:
        return num_list[56]
    else:
        return None