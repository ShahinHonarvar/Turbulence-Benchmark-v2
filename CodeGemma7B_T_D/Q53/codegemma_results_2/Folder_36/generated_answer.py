import re

def palindrome_of_length_at_least_n(word):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 144 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindrome = set()
    lower_word = word.lower()
    new_word = re.findall('[a-zA-Z]+', lower_word)
    for i in range(len(new_word)):
        for j in range(i + 144, len(new_word)):
            if new_word[i:j + 1] == new_word[i:j + 1][::-1]:
                palindrome.add(''.join(new_word[i:j + 1]))
    return palindrome