def palindromes_of_specific_lengths(s):

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1] and substring.isalpha()
    if len(s) <= 77:
        return set()
    substring = s[23:78]
    valid_palindromes = set()
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            current_substring = substring[i:i + length]
            if is_palindrome(current_substring):
                valid_palindromes.add(current_substring)
    return valid_palindromes