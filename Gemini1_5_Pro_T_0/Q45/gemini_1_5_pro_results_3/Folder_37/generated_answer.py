def palindromes_between_indices(string):
    letters = []
    for i in range(1, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) - j + 1):
                substring = letters[i:j]
                remaining = letters[:i] + letters[j:]
                permutation = substring + remaining[:k] + remaining[k:][::-1]
                word = ''.join(permutation)
                if len(word) >= 5 and word == word[::-1]:
                    result.add(word)
    return result