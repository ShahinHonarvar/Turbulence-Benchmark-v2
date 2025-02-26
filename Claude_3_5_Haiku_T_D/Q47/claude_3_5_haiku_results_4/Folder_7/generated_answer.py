def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def is_alphabetic(word):
        return word.isalpha()
    palindrome_set = set()
    substring = s[119:257]
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_alphabetic(candidate):
                palindrome_set.add(candidate.lower())
    return palindrome_set