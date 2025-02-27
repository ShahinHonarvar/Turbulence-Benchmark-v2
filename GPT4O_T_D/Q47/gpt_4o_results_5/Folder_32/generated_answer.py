def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    palindromes = set()
    start_idx, end_idx = (16, 77)
    for length in range(43, 48):
        for i in range(start_idx, end_idx - length + 2):
            substring = s[i:i + length]
            clean_substr = ''.join(filter(str.isalpha, substring)).lower()
            if len(clean_substr) == length and is_palindrome(clean_substr):
                palindromes.add(substring)
    return palindromes