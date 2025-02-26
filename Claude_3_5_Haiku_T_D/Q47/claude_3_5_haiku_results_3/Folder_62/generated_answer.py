def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def contains_only_letters(word):
        return word.isalpha()
    palindromes = set()
    substring = s[26:88].lower()
    for i in range(len(substring)):
        for length in range(52, 57):
            if i + length > len(substring):
                break
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and contains_only_letters(candidate):
                palindromes.add(candidate)
    return palindromes