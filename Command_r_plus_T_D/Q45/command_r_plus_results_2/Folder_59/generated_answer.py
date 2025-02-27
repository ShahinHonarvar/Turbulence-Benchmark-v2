def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(8, min(10, len(s))):
        if s[i].lower() in english_letters:
            for j in range(i + 1, min(i + 3, len(s)) + 1):
                if s[j - 1].lower() in english_letters:
                    palindrome = s[i:j] + s[i:j][::-1]
                    palindromes.add(palindrome)
    return palindromes