def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    s = s[:7].lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for word in alph:
        s = s.replace(word, '')
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes