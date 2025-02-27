def palindromes_between_indices(s):
    s = ''.join(re.findall('[a-zA-Z]', s)).lower()
    if len(s) < 8:
        return set()
    s = s[3:8]
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 1, len(s) - 2):
            if s[i] == s[j] and s[i + 1] == s[j + 1] and (s[i + 2] == s[j + 2]):
                palindromes.add(s[i:i + 4])
    return palindromes