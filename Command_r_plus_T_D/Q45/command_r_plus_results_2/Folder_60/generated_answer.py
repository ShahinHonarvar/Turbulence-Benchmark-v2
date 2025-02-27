def palindromes_between_indices(s):
    sub_str = s[3:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set()
    for i in range(len(sub_str) - 3 + 1):
        for j in range(i + 4, len(sub_str) + 1):
            palindrome = sub_str[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes