def palindromes_between_indices(s):
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    substring = s[0:5]
    substring = ''.join([c for c in substring if c.lower() in english_letters])
    sets = set()
    for i in range(3, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            palindrome = substring[j:j + i]
            if palindrome == palindrome[::-1]:
                sets.add(palindrome.lower())
    return sets