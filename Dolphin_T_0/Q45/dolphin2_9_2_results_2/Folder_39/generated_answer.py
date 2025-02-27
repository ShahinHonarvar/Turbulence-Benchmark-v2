def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = set()
    for i in range(2, 6):
        letters.add(s[i].lower())
    English_letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    palindromes = set()
    for letter in English_letters & letters:
        palindromes.add(letter.lower())
        palindromes.add(letter.upper())
    return palindromes