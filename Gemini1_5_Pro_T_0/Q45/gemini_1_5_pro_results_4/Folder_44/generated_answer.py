def palindromes_between_indices(string):
    letters = []
    for i in range(2, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for s in letters:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                temp = letters[i:j + 1]
                temp.insert(len(temp) // 2, s)
                word = ''.join(temp)
                if len(word) >= 3 and word == word[::-1]:
                    result.add(word)
    return result