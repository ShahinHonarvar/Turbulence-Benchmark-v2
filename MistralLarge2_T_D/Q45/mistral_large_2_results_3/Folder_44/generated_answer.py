def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(len(lower_letters)):
        for j in range(i + 2, len(lower_letters) + 1):
            substring = lower_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes