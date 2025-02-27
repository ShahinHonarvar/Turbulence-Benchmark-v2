def palindromes_between_indices(s):
    letters = set()
    for char in s[6:10]:
        if char.isalpha():
            letters.add(char.lower())

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                if a != c:
                    word = a + b + c
                    if is_palindrome(word):
                        palindromes.add(word)
    return palindromes