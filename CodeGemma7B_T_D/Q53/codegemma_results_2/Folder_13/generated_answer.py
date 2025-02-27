from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    """
    Finds all palindromes of length greater than or equal to 52 in a given string.
    Args:
        text: The text to search for palindromes.
    Returns:
        A set of all palindromes of length greater than or equal to 52 in the given string.
    """
    text = text.lower()
    palindromes = defaultdict(set)
    for i in range(len(text)):
        for j in range(i + 52, len(text) + 1):
            word = text[i:j]
            if word == word[::-1]:
                palindromes[j - i].add(word)
    return set(palindromes.values())