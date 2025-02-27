def palindrome_of_length_n(s):
    """Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 93, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    s = s.lower()
    set_of_palindromes = set()
    for i in range(0, len(s) - 92):
        sub_s = s[i:i + 93]
        if sub_s == sub_s[::-1] and sub_s.isalpha():
            set_of_palindromes.add(sub_s)
    return set_of_palindromes