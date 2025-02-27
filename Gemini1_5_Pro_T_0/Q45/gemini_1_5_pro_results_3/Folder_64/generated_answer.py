def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if 9 < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i):
            substring = letters[j:i]
            if len(substring) >= 5:
                if substring == substring[::-1]:
                    result.add(''.join(substring))
    return result