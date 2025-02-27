def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(5, min(len(s), 9)):
        if s[i].lower() in english_letters:
            for j in range(i - 1, 4, -1):
                if s[j].lower() in english_letters:
                    palindrome = s[j:i + 1]
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes