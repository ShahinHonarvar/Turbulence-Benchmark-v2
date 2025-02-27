def palindromes_of_specific_lengths(s):

    def is_palindrome(w):
        return w == w[::-1]
    substring = s[:8].lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word.isalpha() and is_palindrome(word):
                palindromes.add(word)
    return palindromes