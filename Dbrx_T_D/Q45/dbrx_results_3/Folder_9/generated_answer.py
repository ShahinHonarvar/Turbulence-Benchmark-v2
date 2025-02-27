def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(7):
        for j in range(i, 7 - i):
            substring = s[i:j + 1].lower()
            if set(substring) <= english_letters:
                palindrome = ''.join(sorted(substring, key=substring.index))
                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result