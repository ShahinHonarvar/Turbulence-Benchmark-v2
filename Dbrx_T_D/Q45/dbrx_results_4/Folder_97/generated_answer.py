def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(5):
        for j in range(i, 5):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters and len(substring) >= 3:
                palindrome = ''.join(sorted(substring, reverse=True))
                palindromes.add(palindrome)
    return palindromes