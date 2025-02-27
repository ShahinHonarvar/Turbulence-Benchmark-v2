def palindromes_between_indices(string):
    letters = []
    for i in range(3, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters[i:j]) + 1):
                temp = list(letters[i:j])
                temp.insert(k, letters[i:j])
                word = ''.join(temp)
                if len(word) >= 3 and word == word[::-1]:
                    result.add(word)
    return result