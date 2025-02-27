import re

def palindromes_of_specific_lengths(text):
    """Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string. The given string may consist of any character. The function should return the set of all palindromes with the following requirements. Only palindromes occurring in the substring from index 10 to index 100, both inclusive, should be considered. Only palindromes of lengths between 10 to 50 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    text_lower = text.lower()
    pattern = '(?i)(\\\\b\\\\w{10,50}\\\\b)'
    matches = re.findall(pattern, text_lower[10:101])
    palindromes = set(matches)
    return palindromes