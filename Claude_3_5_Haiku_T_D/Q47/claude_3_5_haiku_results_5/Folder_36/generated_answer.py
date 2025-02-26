def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_letters_only(word):
        return word.isalpha()
    palindromes = set()
    substring = s[124:284].lower()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if is_palindrome(candidate) and is_letters_only(candidate):
                palindromes.add(candidate)
    return palindromes