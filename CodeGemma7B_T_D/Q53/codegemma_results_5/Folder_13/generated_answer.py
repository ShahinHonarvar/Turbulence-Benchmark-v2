import re

def palindrome_of_length_at_least_n(text):
    """
  This function takes a string as an input and returns the set of all palindromes of the length greater than or equal to 52 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
  """
    text = ''.join(re.findall('[a-zA-Z]', text))
    text_lower = text.lower()
    text_split = list(text_lower)
    text_permutations = list(itertools.permutations(text_split))
    palindrome_list = []
    for permutation in text_permutations:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 52:
            palindrome_list.append(palindrome)
    return set(palindrome_list)