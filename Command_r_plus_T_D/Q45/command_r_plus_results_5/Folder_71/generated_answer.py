def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[1:4].lower()
    palindromes = set()
    for i in range(len(s_lower)):
        for j in range(i + 1, len(s_lower)):
            if s_lower[i] == s_lower[j] and s_lower[i] in english_letters:
                palindrome = s_lower[i:j + 1]
                if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes