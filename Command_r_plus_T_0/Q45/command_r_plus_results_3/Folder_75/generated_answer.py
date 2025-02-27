def palindromes_between_indices(s):
    sub_str = s[2:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 1, len(sub_str)):
            palindrome = sub_str[i] + sub_str[j] + sub_str[i]
            palindromes.add(palindrome)
    return palindromes