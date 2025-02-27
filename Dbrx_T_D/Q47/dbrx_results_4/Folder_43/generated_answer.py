def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return c.lower() >= 'a' and c.lower() <= 'z'

    def is_palindrome(s):
        i, j = (0, len(s) - 1)
        while i < j:
            if not is_english_letter(s[i]):
                i += 1
                continue
            if not is_english_letter(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
    palindromes = set()
    for length in range(23, 39):
        for start in range(41, 90 - length + 1):
            if is_palindrome(s[start:start + length]):
                palindromes.add(s[start:start + length])
    return palindromes