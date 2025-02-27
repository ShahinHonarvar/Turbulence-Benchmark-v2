def palindromes_between_indices(string):
    letters = []
    for i in range(0, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(0, len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(0, len(substring) + 1):
                for l in range(k + 1, len(substring) + 1):
                    candidate = substring[0:k] + list(reversed(substring[k:l])) + substring[l:]
                    if len(candidate) >= 4:
                        word = ''.join(candidate)
                        if word == word[::-1]:
                            result.add(word)
    return result