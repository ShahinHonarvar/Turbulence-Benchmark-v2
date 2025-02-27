def palindrome_of_length_n(s):
    """
    Finds all palindromes of length 95 in a given string.
    """

    def is_palindrome(word):
        """
        Checks if a word is a palindrome.
        """
        return word == word[::-1]

    def find_palindromes(s, current_word, remaining_length):
        """
        Recursively finds palindromes of length remaining_length.
        """
        if remaining_length == 0 and is_palindrome(current_word):
            palindromes.add(current_word)
            return
        for i in range(len(s)):
            if s[i].isalpha():
                new_word = current_word + s[i]
                find_palindromes(s[i + 1:], new_word, remaining_length - 1)
    palindromes = set()
    find_palindromes(s.lower(), '', 95)
    return palindromes