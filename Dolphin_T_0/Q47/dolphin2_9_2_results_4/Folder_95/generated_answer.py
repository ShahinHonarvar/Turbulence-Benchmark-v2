def palindromes_of_specific_lengths(s):
    s = s[11:57]
    palindromes = set()
    for i in range(20, 22):
        for j in range(len(s) - i + 1):
            if all((c.isalpha() for c in s[j:j + i])) and s[j:j + i].lower() == s[j:j + i][::-1].lower():
                palindromes.add(s[j:j + i])
    return palindromes