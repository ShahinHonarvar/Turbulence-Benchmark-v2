def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]

    def extract_english_letters(s):
        return ''.join(filter(str.isalpha, s))
    s = s[11:94].lower()
    palindromes = set()
    for length in range(34, 55):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            substring_letters = extract_english_letters(substring)
            if len(substring_letters) == length and is_palindrome(substring_letters):
                palindromes.add(substring_letters)
    return palindromes