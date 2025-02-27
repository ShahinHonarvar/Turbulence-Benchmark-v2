def palindromes_between_indices(s):
    s = s.lower()
    letters = []
    for i in range(1, 8):
        if s[i].isalpha() and s[i] in 'abcdefghijklmnopqrstuvwxyz':
            letters.append(s[i])
    result = set()
    if len(letters) < 3:
        return result
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                temp = letters[i] + letters[j] + letters[k]
                if temp[::-1] == temp:
                    result.add(temp)
                temp = letters[i] + letters[k] + letters[j]
                if temp[::-1] == temp:
                    result.add(temp)
                temp = letters[j] + letters[i] + letters[k]
                if temp[::-1] == temp:
                    result.add(temp)
                temp = letters[j] + letters[k] + letters[i]
                if temp[::-1] == temp:
                    result.add(temp)
                temp = letters[k] + letters[i] + letters[j]
                if temp[::-1] == temp:
                    result.add(temp)
                temp = letters[k] + letters[j] + letters[i]
                if temp[::-1] == temp:
                    result.add(temp)
    return result