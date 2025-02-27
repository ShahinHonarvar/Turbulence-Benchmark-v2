def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if len(s) < 4 or not 2 <= 4 <= len(s):
        return set()
    target_letters = {c for c in s[2:5] if c in english_letters}
    if len(target_letters) < 2:
        return set()
    palindromes = set()
    for i in range(3):
        for j in range(i, 5 - i):
            if s[2 + i] != s[3 + i - j] or s[2 + i] not in target_letters or s[3 + i - j] not in target_letters:
                continue
            palindrome = s[2 + i:3 + i - j:-1] + s[2 + i:3 + i - j]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes