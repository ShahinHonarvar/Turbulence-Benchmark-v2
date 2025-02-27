from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    """
    Returns the set of all palindromes of the length greater than or equal to 18 that exist in the given string.
    Each palindrome should only consist of English letters.
    If no such palindromes exist in the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    char_to_indices = defaultdict(list)
    for i, char in enumerate(text):
        if char.isalpha():
            char_to_indices[char].append(i)
    palindromes = set()
    for char, indices in char_to_indices.items():
        for i in range(len(indices)):
            for j in range(i + 2, len(indices)):
                if text[indices[i]:indices[j]] == text[indices[j]:indices[i]:-1]:
                    palindrome = text[indices[i]:indices[j] + 1]
                    if len(palindrome) >= 18:
                        palindromes.add(palindrome)
    return palindromes