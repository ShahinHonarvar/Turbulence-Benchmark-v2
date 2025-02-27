def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def clean_string(s):
        return ''.join(filter(str.isalpha, s)).lower()
    substr_palindromes = set()
    s = clean_string(s[11:98])
    for start in range(len(s)):
        for end in range(start + 29, min(start + 63, len(s) + 1)):
            candidate = s[start:end]
            if is_palindrome(candidate):
                substr_palindromes.add(s[start:end])
    return substr_palindromes