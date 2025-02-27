def palindromes_between_indices(s):
    s = s[3:5].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for j in range(len(s) - i + 1):
            substr = s[j:j + i]
            for k in range(len(substr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if substr[k] != c:
                        new_substr = substr[:k] + c + substr[k + 1:]
                        if new_substr == new_substr[::-1]:
                            palindromes.add(new_substr)
    return palindromes