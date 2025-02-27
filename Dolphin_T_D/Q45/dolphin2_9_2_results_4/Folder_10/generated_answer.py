def palindromes_between_indices(s):
    s = s[:6].lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            p = s[i:j + 1]
            for letter in p:
                if letter not in alphabet:
                    break
            else:
                palindromes.add(p)
    return palindromes