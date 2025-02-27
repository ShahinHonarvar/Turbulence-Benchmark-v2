def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s_lower = s[2:5].lower()
    for i in range(len(s_lower)):
        for j in range(i + 1, len(s_lower)):
            if s_lower[i] in english_letters and s_lower[j] in english_letters:
                palindrome = s_lower[i:j + 1]
                if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes