def palindrome_of_length_n(text):
    """
    This function takes one argument, a string, and returns the set of all palindromes of the length equal 
    to 474, where each palindrome is a substring of the given string. Each palindrome should only consist of 
    English letters. If there is no palindrome of the specified length as a substring of the given string, the 
    function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    substring = text[i:l + 1]
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes