import string

def palindromes_between_indices(s):
    letters = set()
    substring = s[3:9]
    for letter in substring:
        if letter in string.ascii_letters:
            letters.add(letter.lower())
    palindromes = set()
    for i in range(6, len(substring) + 1):
        for p in combinations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes