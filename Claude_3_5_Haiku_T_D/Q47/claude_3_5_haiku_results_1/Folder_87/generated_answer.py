def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters(word):
        return word.isalpha()
    palindromes = set()
    for start in range(11, 94):
        for length in range(34, 55):
            end = start + length
            if end > len(s):
                break
            substring = s[start:end].lower()
            if is_palindrome(substring) and is_english_letters(substring):
                palindromes.add(substring)
    return palindromes