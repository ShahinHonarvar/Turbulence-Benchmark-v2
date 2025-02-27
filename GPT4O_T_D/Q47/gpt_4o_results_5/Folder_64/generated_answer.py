def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def only_letters(sub):
        return ''.join([c for c in sub if c.isalpha()])
    s = s[:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(4, 6):
            if i + length <= len(s):
                sub = s[i:i + length]
                sub_letters = only_letters(sub)
                if len(sub_letters) == length and is_palindrome(sub_letters):
                    palindromes.add(sub_letters)
    return palindromes