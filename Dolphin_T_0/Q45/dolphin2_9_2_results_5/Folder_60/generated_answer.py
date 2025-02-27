def palindromes_between_indices(s):
    letters = s[3:7]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, 0, -1):
        for i in range(len(letters) - length + 1):
            word = letters[i:i + length]
            if len(set(word.lower())) == 26:
                palindromes.add(word)
                palindromes.add(word[::-1])
                break
    return palindromes