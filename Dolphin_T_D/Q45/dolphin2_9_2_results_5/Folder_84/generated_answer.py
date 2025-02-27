def palindromes_between_indices(s):
    sub_s = s[4:10]
    sub_s = ''.join((ch for ch in sub_s if ch.isalpha()))
    if len(sub_s) < 3:
        return set()
    sub_s = sub_s.lower()
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(i + 2, len(sub_s) + 1):
            substring = sub_s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes