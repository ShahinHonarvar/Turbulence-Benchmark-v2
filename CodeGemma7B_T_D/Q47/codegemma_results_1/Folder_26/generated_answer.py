def palindromes_of_specific_lengths(s):
    if not s or len(s) < 21 or len(s) > 84:
        return set()

    def is_palindrome(word):
        return word == word[::-1] and word.isalpha()
    palindromes = set()
    for i in range(24, 84 + 1):
        for j in range(i - 20, i + 1):
            word = s[j:i + 1].lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes