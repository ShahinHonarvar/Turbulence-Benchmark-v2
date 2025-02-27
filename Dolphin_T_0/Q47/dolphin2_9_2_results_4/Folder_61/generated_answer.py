def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    def is_english_letter(c):
        return c.isalpha()
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if all((is_english_letter(c) for c in sub)) and is_palindrome(sub):
                palindromes.add(sub)
                if i < len(s) - length:
                    break
    return palindromes