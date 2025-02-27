def palindromes_between_indices(s):
    letters = s[4:7]
    for c in letters:
        if not c.isalpha():
            return set()
    letters = ''.join(sorted(letters.lower()))
    if len(set(letters)) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            if letters.count(letters[i]) > 1 and letters[i] == letters[j]:
                continue
            for k in range(len(letters[i:j + 1]) - 1):
                mid = letters[i:j + 1][k]
                if letters.count(mid) == 1:
                    continue
                for p in range(len(letters[:i]) + len(letters[j + 1:])):
                    temp = letters[:i] + mid + letters[i:j + 1][:k] + (letters[j + 1:] if k + 1 == len(letters[i:j + 1]) else letters[j + 1:])
                    temp = temp.swapcase()
                    if temp[::-1] == temp:
                        palindromes.add(temp)
    return palindromes