def palindrome_of_length_n(string):
    """
    Finds the set of all palindromes of the length equal to 210, where each palindrome is a substring of the given string.
    Each palindrome should only consist of English letters.
    If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 210 + 1):
        substring = string[i:i + 210]
        is_palindrome = True
        for j in range(len(substring) // 2):
            if substring[j] != substring[len(substring) - j - 1]:
                is_palindrome = False
                break
        if is_palindrome:
            palindromes.add(substring)
    return palindromes