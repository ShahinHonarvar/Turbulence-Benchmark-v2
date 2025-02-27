def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring) + 1):
                for l in range(len(substring) + 1):
                    candidate = substring[:k] + substring[l:]
                    if len(candidate) >= 5:
                        if candidate == candidate[::-1]:
                            result.add(''.join(candidate))
    return result