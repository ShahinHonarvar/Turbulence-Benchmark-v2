def palindromes_between_indices(string):
    letters = []
    for i in range(0, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 3:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[len(substring) - k - 1]:
                        break
                else:
                    permutation = ''.join(substring)
                    result.add(permutation)
    return result