from nltk import ngrams

def palindrome_of_length_n(text, palindrome_length):
    """
    Finds all palindromes of the specified length in a given string.

    Args:
    text: The string to find palindromes in.
    palindrome_length: The length of the palindromes to find.

    Returns:
    The set of all palindromes of the specified length in the given string.
    """
    text = text.lower()
    ngrams_list = list(ngrams(text, palindrome_length))
    palindromes = set()
    for ngram in ngrams_list:
        if ngram[:] == ngram[::-1]:
            palindromes.add(''.join(ngram))
    return palindromes