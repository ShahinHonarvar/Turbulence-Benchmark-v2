def palindromes_between_indices(s):
    letters_between_indices = set(s[4:9].lower())
    n = len(letters_between_indices)
    if n < 2:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            if letters_between_indices.pop() == letters_between_indices.pop():
                palindromes.add(s[4:5 + i:j - i])
            else:
                return set()
    return palindromes