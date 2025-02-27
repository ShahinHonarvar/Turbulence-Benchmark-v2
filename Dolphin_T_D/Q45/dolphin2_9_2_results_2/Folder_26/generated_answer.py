def palindromes_between_indices(s):
    letters = [ch for ch in s if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z']
    if len(letters) < 3:
        return set()
    middle = ''.join([ch for ch in s[4:7] if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z'])
    length = len(middle)
    if length < 3:
        return set()
    palindromes = set()
    for p in range(length):
        for q in range(p, length):
            if middle[p:q + 1] == middle[p:q + 1][::-1]:
                palindromes.add(middle[p:q + 1].lower())
    return palindromes