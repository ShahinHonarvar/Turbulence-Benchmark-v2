def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring == substring[::-1] and substring.isalpha()
    palindrome_set = set()
    substring = s[100:301].lower()
    for length in range(50, 101):
        for start in range(len(substring) - length + 1):
            current_substring = substring[start:start + length]
            if is_palindrome(current_substring):
                palindrome_set.add(current_substring)
    return palindrome_set