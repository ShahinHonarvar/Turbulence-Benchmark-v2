def palindromes_between_indices(s):
    palindromes = set()
    substr = s[2:9].lower()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    valid_letters = letters.intersection(set(substr))
    if len(valid_letters) < 7:
        return palindromes
    for i in range(7, len(valid_letters) + 1):
        for comb in itertools.combinations(valid_letters, i):
            palindrome = ''.join(comb)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes