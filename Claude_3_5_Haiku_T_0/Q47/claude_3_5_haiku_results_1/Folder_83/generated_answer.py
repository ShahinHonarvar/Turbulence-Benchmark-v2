def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_only_letters(word):
        return word.isalpha()
    result = set()
    substring = s[75:96].lower()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and is_only_letters(candidate):
                result.add(candidate)
    return result