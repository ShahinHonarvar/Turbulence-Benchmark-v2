def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:10].lower()
    s_set = set(s_lower)
    palindromes = set()
    for i in range(3, 6):
        for j in range(i + 1, 7):
            for k in range(j + 1, 8):
                if s_set.issubset(english_letters) and s_lower[i] == s_lower[j] == s_lower[k]:
                    palindrome = s_lower[i:k + 1]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes