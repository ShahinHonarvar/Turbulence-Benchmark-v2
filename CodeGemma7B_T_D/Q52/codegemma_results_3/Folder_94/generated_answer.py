def palindrome_of_length_n(str):
    """
    Returns the set of all palindromes of the length equal to 93, where
    each palindrome is a substring of the given string. Each palindrome
    should only consist of English letters. If there is no palindrome of the
    specified length as a substring of the given string, the function
    should return an empty set. The function should find
    the palindromes in a case-insensitive manner.
    """
    palindrome_list = []
    str = str.lower()
    length = len(str)
    if length < 93:
        return set()
    for i in range(length - 93 + 1):
        substring = str[i:i + 93]
        if substring == substring[::-1]:
            palindrome_list.append(substring)
    return set(palindrome_list)