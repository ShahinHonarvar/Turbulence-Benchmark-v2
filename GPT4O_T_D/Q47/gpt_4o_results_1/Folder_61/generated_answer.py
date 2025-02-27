def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_letters(sub):
        return ''.join(filter(str.isalpha, sub))
    for start in range(12):
        for end in range(start + 20, min(start + 31, 31)):
            substring = extract_letters(s[start:end + 1])
            if 20 <= len(substring) <= 30 and is_palindrome(substring):
                result.add(substring)
    return result