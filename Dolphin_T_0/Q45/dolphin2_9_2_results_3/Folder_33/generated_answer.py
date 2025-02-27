def palindromes_between_indices(s):
    sub = s[7:10]
    letters = [c.lower() for c in sub if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        substring = ''.join(letters[i:])
        while len(substring) >= 4:
            if substring == substring[::-1] and substring not in palindromes:
                palindromes.add(substring)
            substring = substring[-1] + substring[:-1]
    return palindromes