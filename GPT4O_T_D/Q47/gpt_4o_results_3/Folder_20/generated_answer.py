def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def extract_letters(sub):
        return ''.join((c for c in sub if c.isalpha()))
    palindromes_set = set()
    s = s.lower()
    for start in range(20, 75):
        for length in range(36, 43):
            end = start + length
            if end > 75:
                break
            substring = extract_letters(s[start:end])
            if is_palindrome(substring) and 36 <= len(substring) <= 42:
                palindromes_set.add(substring)
    return palindromes_set