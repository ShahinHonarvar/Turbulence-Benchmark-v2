def palindromes_between_indices(string):
    letters = []
    for i in range(3, 10):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i):
            substring = letters[j:i]
            if len(substring) >= 7:
                if substring == substring[::-1]:
                    result.add(''.join(substring))
    return result