def palindromes_between_indices(s):
    s = s[1:9].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s)
    common_letters = s_letters & english_letters
    s = ''.join(sorted(common_letters))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes