import itertools

def all_substring_of_size_n(str1):
    """
    :type str1: str
    """
    substr = []
    for i in range(len(str1) - 90):
        for j in range(i + 91):
            if len(set(str1[i:j + 1])) == 91:
                substr.append(str1[i:j + 1])
    return substr