def palindromes_between_indices(s):
    sub_str = s[5:8].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join(filter(english_letters.__contains__, sub_str))
    palindromes = set()
    for i in range(len(sub_str) - 1):
        for j in range(i + 2, len(sub_str) + 1):
            palindrome = sub_str[i:j]
            if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes