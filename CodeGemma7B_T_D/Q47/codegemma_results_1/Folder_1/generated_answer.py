def palindromes_of_specific_lengths(str):
    """This function takes string and returns set of palindromes of specific lengths and indices"""
    result = set()
    for word in str[15:89 + 1].lower().split():
        if len(word) >= 40 and len(word) <= 72 and (word == word[::-1]):
            result.add(word)
    return result