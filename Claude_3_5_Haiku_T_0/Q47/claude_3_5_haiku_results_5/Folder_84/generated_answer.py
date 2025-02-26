def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letters_only(word):
        return word.isalpha()
    palindromes = set()
    if len(s) < 78:
        return palindromes
    substring = s[23:78]
    for length in range(13, 41):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length].lower()
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes