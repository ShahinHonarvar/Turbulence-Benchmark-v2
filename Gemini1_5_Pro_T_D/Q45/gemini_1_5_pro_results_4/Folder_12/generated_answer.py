def palindromes_between_indices(string):
    s = string[3:9].lower()
    letters = []
    for c in s:
        if c.isalpha():
            letters.append(c)
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 4:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[len(substring) - k - 1]:
                        break
                else:
                    result.add(''.join(substring))
    return result