def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[8:10]))
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for p in range(length):
        for q in range(p, length):
            if letters[p:q + 1] == letters[p:q + 1][::-1]:
                palindromes.add(letters[p:q + 1])
    return palindromes