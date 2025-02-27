def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    begin, end = (6, 9)
    if end > len(s):
        return set()
    substr = s[begin:end + 1].lower()
    palindromes = set()
    for i in range(len(substr) - 2):
        for j in range(i + 3, len(substr) + 1):
            subsub = substr[i:j]
            if set(subsub) <= english_letters:
                if subsub == subsub[::-1]:
                    palindromes.add(subsub)
    return palindromes