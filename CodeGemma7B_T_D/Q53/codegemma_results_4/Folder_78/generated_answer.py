def palindrome_of_length_at_least_n(sentence):
    """
    The function takes in a string and returns the set of all palindromes of length >= 96.
    """
    sentence = sentence.lower()
    padding_len = 96 - 1
    palindromes = set()
    for i in range(len(sentence) - padding_len):
        substring = sentence[i:i + 2 * padding_len + 1]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes