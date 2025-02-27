def palindrome_of_length_at_least_n(s):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 85 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    lower_s = s.lower()
    palindromes = set()
    for i in range(len(lower_s)):
        for j in range(i + 85, len(lower_s) + 1):
            substring = lower_s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes