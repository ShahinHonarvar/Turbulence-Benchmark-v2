def palindromes_between_indices(string):
    letters = []
    for i in range(1, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for l in range(k, len(substring) + 1):
                    permutation = substring[k:l] + substring[:k] + substring[l:]
                    if len(permutation) >= 7:
                        if permutation == permutation[::-1]:
                            result.add(''.join(permutation))
    return result