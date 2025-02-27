def palindromes_between_indices(string):
    letters = []
    for i in range(2, 6):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i):
            substring = letters[j:i]
            if len(substring) >= 5:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[len(substring) - k - 1]:
                        break
                else:
                    result.add(''.join(substring))
    return result