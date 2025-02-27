def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(1, min(10, len(s))):
        substring = s[1:i + 1]
        substring_letters = set(substring.lower())
        if substring_letters.issubset(english_letters):
            palindrome = ''.join(substring_letters)
            if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes