def palindromes_between_indices(s):
    sub_str = s[3:5].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set()
    for i in range(len(filtered_sub_str)):
        for j in range(i + 3, len(filtered_sub_str) + 1):
            palindrome = filtered_sub_str[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes