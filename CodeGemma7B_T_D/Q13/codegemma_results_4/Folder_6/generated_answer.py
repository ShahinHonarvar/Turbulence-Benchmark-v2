def find_second_largest_num(numbers):
    """
    This function takes a list of distinct numbers as input and returns the second largest element from index 10 to index 66, both inclusive. If there is no such element, the function should return 'None'.
    """
    sublist = numbers[10:67]
    if not sublist:
        return 'None'
    sublist.sort(reverse=True)
    return sublist[1]