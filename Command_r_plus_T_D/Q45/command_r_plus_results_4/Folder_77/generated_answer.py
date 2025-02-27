def palindromes_between_indices(s):
    sub_str = s[4:7].lower()
    english_set = set('abcdefghijklmnopqrstuvwxyz')
    filtered_sub_str = ''.join(filter(english_set.__contains__, sub_str))
    palindromes = set()
    for i in range(len(filtered_sub_str) - 1, 0, -1):
        for j in range(i + 1):
            palindrome = filtered_sub_str[j:i] + filtered_sub_str[i - 1:j - 1:-1]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes