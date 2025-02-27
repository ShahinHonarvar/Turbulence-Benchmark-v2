def palindromes_between_indices(s):
    letters = list(s[1:5].lower())
    palindromes = set()
    for p in permutations(letters, 5):
        content = ''.join(p)
        if content == content[::-1]:
            palindromes.add(content)
    return palindromes