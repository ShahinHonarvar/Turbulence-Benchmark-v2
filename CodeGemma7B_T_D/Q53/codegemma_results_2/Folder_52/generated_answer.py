import re
    import itertools

def palindrome_of_length_at_least_n(s):
    """
    Returns the set of all palindromes of the length greater than or equal to 14 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    s = s.lower()
    pattern = re.compile('(?=(.*?)(?<![^a-z])[\\\\w]{14,}\\\\b(?<![^a-z])(.*?))')
    matches = pattern.findall(s)
    palindromes = set()
    for match in matches:
        if re.match('^[a-z]+$', match[0]):
            palindromes.add(match[0])
    return palindromes