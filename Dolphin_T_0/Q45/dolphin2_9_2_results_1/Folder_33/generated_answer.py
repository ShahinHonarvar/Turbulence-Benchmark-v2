def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = s[6:10]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub = substring[i:j]
            if len(set(sub.lower()) - english_letters) == 0:
                palindromes.add(sub)
    return palindromes