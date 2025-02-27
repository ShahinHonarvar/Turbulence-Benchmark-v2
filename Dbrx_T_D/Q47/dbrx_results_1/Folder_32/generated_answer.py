def palindromes_of_specific_lengths(s):

    def is_english_letter(c):
        return c.lower().isalpha()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(16, 78):
        for length in range(43, 48):
            if i + length - 1 <= 77:
                sub_str = s[i:i + length]
                if all((is_english_letter(c) for c in sub_str)) and is_palindrome(sub_str):
                    palindromes.add(sub_str)
    return palindromes