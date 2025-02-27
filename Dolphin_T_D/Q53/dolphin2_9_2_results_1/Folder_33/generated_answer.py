def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letter(ch):
        return ch.isalpha()
    if not s:
        return set()
    s = s.lower()
    palindromes = set()
    n = 141
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            word = s[i:j]
            if is_palindrome(word) and all((is_english_letter(ch) for ch in word)):
                palindromes.add(word)
    return palindromes