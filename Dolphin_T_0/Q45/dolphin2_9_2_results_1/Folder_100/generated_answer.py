def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def can_form_palindrome(word):
        char_freq_str = ''.join(sorted([char for char in word]))
        char_freq_substr = ''.join(sorted([char for char in s[0:6]]))
        return is_palindrome(char_freq_str) and is_palindrome(char_freq_substr)
    substr = s[0:6]
    palindromes = set()
    for i in range(6):
        for j in range(i + 1, 7):
            if can_form_palindrome(substr[i:j]):
                palindromes.add(substr[i:j])
    return palindromes