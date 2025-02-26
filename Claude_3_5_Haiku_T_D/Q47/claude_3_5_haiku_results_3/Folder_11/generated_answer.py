def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]

    def is_letters_only(substring):
        return substring.isalpha()
    substring = s[24:98]
    palindrome_set = set()
    for length in range(10, 37):
        for start in range(len(substring) - length + 1):
            current_substring = substring[start:start + length]
            if is_palindrome(current_substring) and is_letters_only(current_substring):
                palindrome_set.add(current_substring.lower())
    return palindrome_set