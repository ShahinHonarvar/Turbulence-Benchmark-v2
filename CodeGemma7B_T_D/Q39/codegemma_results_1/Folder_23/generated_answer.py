def return_n_greatest_chars(str1):
    """A function that returns a sorted list of 46 characters of the given string with the greatest ascii values"""
    n_all_ascii = []
    for i in str1:
        n_all_ascii.append(ord(i))
    n_all_ascii.sort()
    return n_all_ascii[-46:]