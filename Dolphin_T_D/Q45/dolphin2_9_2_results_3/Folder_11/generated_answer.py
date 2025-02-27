def palindromes_between_indices(s):
    string = s[3:8]
    letters = [i for i in string if i.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if len(substring) >= 4 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes