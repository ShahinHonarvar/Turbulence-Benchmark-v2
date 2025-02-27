def palindromes_between_indices(string):
    letters = []
    for i in range(3, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for l in range(k, len(substring) + 1):
                    permutation = substring[k:l] + substring[:k] + substring[l:]
                    if len(permutation) >= 4 and permutation == permutation[::-1]:
                        result.add(''.join(permutation))
    return result