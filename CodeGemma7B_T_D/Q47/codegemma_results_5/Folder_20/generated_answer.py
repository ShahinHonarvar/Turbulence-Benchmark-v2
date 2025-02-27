from typing import Set

def palindromes_of_specific_lengths(text: str) -> Set[str]:
    """
    This function takes one argument, a string. It returns the set of all palindromes with the following requirements. Only palindromes occurring in the substring from index 20 to index 74, both inclusive, should be considered. Only palindromes of lengths between 36 to 42 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    substrings = [text[i:i + l] for i in range(20, 75) for l in range(36, 43)]
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes