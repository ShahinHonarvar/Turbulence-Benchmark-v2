def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:7] if char.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            p = letters[i:j + 1]
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes