def palindromes_between_indices(s):
    letters = set(s[8:10].lower())
    result = set()
    for length in range(3, len(s[8:10]) + 1):
        for word in (''.join(i) for i in product(letters, repeat=length)):
            if word == word[::-1]:
                result.add(word)
    return result