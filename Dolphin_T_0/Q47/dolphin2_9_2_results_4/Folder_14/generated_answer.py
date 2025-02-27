def palindromes_of_specific_lengths(string):
    substring = string[10:75]

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters(word):
        return all((c.isalpha() for c in word))
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(substring) - length):
            word = substring[i:i + length]
            if is_palindrome(word) and is_english_letters(word):
                palindromes.add(word.lower())
    return palindromes