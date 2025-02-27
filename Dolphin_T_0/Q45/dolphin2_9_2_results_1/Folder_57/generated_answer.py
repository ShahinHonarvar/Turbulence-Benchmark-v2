def palindromes_between_indices(s):
    string_part = s[2:6]
    english_letters = [x for x in string_part.lower() if x.isalpha()]
    n = len(english_letters)
    palindromes = set()
    if n >= 5:
        for i in range(n):
            for j in range(i + 5, n + 1):
                substring = ''.join(english_letters[i:j])
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes