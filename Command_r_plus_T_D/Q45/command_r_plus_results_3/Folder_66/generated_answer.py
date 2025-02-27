def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s[:6])):
        if s[i] in english_letters:
            for j in range(i + 1, len(s[:6])):
                if s[j] in english_letters:
                    palindrome = s[i:j + 1]
                    if palindrome == palindrome[::-1] and len(palindrome) >= 5:
                        palindromes.add(palindrome)
    return palindromes