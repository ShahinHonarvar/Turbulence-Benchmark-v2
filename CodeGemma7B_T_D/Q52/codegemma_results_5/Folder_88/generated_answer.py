def palindrome_of_length_n(s):
    """
    Finds all palindromes of the specified length as substrings of the given string.
    
    The function takes one argument, a string, and returns the set of all palindromes in
    the specified length. The returned set is always either empty or non-empty in order to
    avoid unnecessary complexity.
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 12):
        substring = s[i:i + 13]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes