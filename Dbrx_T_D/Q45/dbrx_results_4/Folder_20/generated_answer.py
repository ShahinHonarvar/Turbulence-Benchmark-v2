def palindromes_between_indices(s):
    pattern = re.compile('[a-zA-Z]', re.ASCII)
    letters = pattern.findall(s[2:9])
    if len(letters) < 4:
        return set()
    palindromes = {letters[i] + letters[i + j] + letters[i] for i in range(len(letters) - 1) for j in range(1, len(letters) - i) if i + j < len(letters)}
    palindromes = {p for p in palindromes if p[1] == p[2]}
    return palindromes