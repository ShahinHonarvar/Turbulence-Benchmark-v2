import re
    import itertools

def palindromes_between_indices(text):
    """
    This function takes a string and returns a set of all palindromes of the length of at least 4
    such that each palindrome is created from any possible arrangement of the English letters
    in the given string that occur between index 0 to index 4, both inclusive.
    """
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 5:
        return set()
    palindromes = set()
    for i in range(len(text) - 3):
        for j in range(i + 1, len(text) - 2):
            for k in range(j + 1, len(text) - 1):
                for l in range(k + 1, len(text)):
                    word = text[i:l + 1]
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes