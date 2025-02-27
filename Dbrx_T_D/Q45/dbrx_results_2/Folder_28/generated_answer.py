def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, min(5, len(s))):
        for j in range(i, min(6, len(s) + 1)):
            substring = s[i:j].lower()
            if english_letters >= set(substring):
                palindrome = ''.join(sorted(substring, reverse=True))
                if palindrome != substring:
                    substring = substring + palindrome[len(substring):]
                if len(substring) >= 4:
                    palindromes.add(substring)
    return palindromes