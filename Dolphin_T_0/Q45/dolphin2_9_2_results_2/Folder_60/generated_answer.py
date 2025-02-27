def palindromes_between_indices(s):
    set_palindromes = set()
    s = s[3:7]
    for i in range(len(s)):
        for j in range(i + 4, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 4 and substring == substring[::-1]:
                set_palindromes.add(substring.lower())
    return set_palindromes