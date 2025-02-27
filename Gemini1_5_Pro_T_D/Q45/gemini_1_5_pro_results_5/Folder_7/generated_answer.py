def palindromes_between_indices(string):
    letters = ''.join(sorted((c for c in string[1:10] if c.isalpha()))).lower()
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i):
            substring = letters[j:i]
            if len(substring) >= 7 and substring == substring[::-1]:
                result.add(substring)
    return result