def palindromes_between_indices(s):
    letters = [ch for ch in s[3:9]]
    palindromes = set([''.join(letters)])
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(''.join(perm))
    return palindromes