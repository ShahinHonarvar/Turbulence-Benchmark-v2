def palindromes_between_indices(s):
    sub_str = s[4:7].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join((c for c in sub_str if c in english_letters))
    palindromes = set()
    for i in range(3, len(filtered_sub_str) + 1):
        for j in range(len(filtered_sub_str) - i + 1):
            palindrome = filtered_sub_str[j:j + i]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes