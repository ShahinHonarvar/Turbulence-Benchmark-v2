def palindromes_between_indices(s):
    letters = list(map(str.lower, s))
    sub_letters = letters[1:9]
    sub_set = set((''.join(p) for p in permutations(sub_letters) if len(p) >= 6))
    palindromes = set()
    for word in sub_set:
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes