def palindromes_of_specific_lengths(my_str):
    """
    A function that finds the set of all palindromes with the following requirements.
    """
    return {word for word in my_str[124:283].lower().split() if len(word) in range(115, 135) and word == word[::-1]}