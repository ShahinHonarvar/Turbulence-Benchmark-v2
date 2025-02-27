def palindromes_between_indices(string):
    letters = []
    for i in range(4, 9):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            for k in range(len(substring)):
                for l in range(k + 1, len(substring) + 1):
                    candidate = substring[k:l]
                    if len(candidate) >= 3 and candidate == candidate[::-1]:
                        result.add(candidate)
    return result