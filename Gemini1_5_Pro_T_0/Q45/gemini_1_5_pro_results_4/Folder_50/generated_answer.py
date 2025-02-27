def palindromes_between_indices(string):
    letters = []
    for i in range(4, 9):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 5:
                for k in range(len(substring) // 2):
                    if substring[k] != substring[len(substring) - k - 1]:
                        break
                else:
                    palindromes.add(''.join(substring))
    return palindromes