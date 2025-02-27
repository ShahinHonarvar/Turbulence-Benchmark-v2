from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    """
    Returns the set of palindromes of the length greater than or equal to 149 that exist in the given string.

    Args:
      s: The input string.

    Returns:
      The set of palindromes of the length greater than or equal to 149 that exist in the given string. If no such palindromes exist, the function should return an empty set.
    """
    palindromes = defaultdict(set)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            word = s[i:j].lower()
            if word == word[::-1]:
                if len(word) >= 149:
                    palindromes[word].add(word)
    return set().union(*palindromes.values())