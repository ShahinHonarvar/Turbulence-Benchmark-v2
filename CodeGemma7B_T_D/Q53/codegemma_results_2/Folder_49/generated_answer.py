def palindrome_of_length_at_least_n(s):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 73 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, -1, -1):
            if s[i] == s[j]:
                length = j + 1 - i
                if length >= 73:
                    palindromes.add(s[i:j + 1])
    return palindromes