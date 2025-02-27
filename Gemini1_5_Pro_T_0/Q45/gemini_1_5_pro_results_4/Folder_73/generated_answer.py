def palindromes_between_indices(string):
    letters = []
    for i in range(3, 7):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(1, len(substring) + 1):
                for permutation in itertools.permutations(substring, k):
                    word = ''.join(permutation)
                    if len(word) >= 3 and word == word[::-1]:
                        result.add(word)
    return result