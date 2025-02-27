def palindromes_between_indices(s):
    letter_set = set()
    for i in range(4, 7):
        letter_set.add(s[i].lower())
    if len(letter_set) < 3:
        return set()
    palindromes = set()
    for word in letter_set:
        palindromes.add(word * (len(word) // 2 + len(word) % 2))
    return palindromes